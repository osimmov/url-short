import json
import urllib.parse
import urllib.request

file_path = 'url.json'

user_input = input("1.'s' to shorten a link\n2.'c' to check the list of links\n3.'o' original link\n4.'q' to quit:\n")
while user_input != 'q':
    if user_input == 's':
        link = input("Enter the link: ")

        # Validate URL
        with urllib.request.urlopen(link) as response:
            if response.status != 200:
                print("Invalid URL. Please try again.")
        
        # Short link
        encoded_link = urllib.parse.quote(link, safe='') #Encode the link
        short_link = f"https://short.url/{encoded_link[-9:]}" # Create a short link using the last 6 characters of the encoded link
        print(f"Shortened link: {short_link}")
        
        # Save to json
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)# Load existing data
        data.update({short_link: link})# Add new link
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4) # Save updated data
        
        print("\nLink saved.\n")
    
    if user_input == 'c':
        with open(file_path, 'r') as json_file:
            data = json.load(json_file) # Load existing data
        print(f"\nLinks found:{len(data)} \n") # Print number of links
    
    if user_input == 'o':
        short_link = input("Enter the shortened link: ")
        with open(file_path, 'r') as json_file:
            data = json.load(json_file) # Load existing data
        original_link = data.get(short_link)
        if original_link:
            print(f"Original link: {original_link}\n")
        else:
            print("Shortened link not found.\n")
    user_input = input("1.'s' to shorten a link\n2.'c' to check the list of links\n3.'o' original link\n4.'q' to quit:\n")

#End