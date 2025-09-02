# URL Shortener

This program is a simple project that takes a link and returns its shortened version.
It first checks the validity of the link using the urllib.request library. If the response status code is 200, the program proceeds; otherwise, it notifies the user that the link is invalid.

For valid links, the program encodes the URL using the urllib.parse library and appends the last 9 characters of the encoded string to the template domain https://short.url/. This approach helps prevent repetition and ensures the uniqueness of each shortened link.

All links are saved in a JSON file in the following format:
{
    shortened_link: original link,
    shortened_link: original link,
    shortened_link: original link
}


## Features
- Shorten the URLs
- Retrieve the original link
- Display how many links were shortened
- Quit the program

## Installation
To run the program you have to clone the repository using the terminal and git commands.
1. Copy the repo link
2. Go to the terminal and run "git clone https://github.com/osimmov/url-short.git"

##Usage
1. To run the program, open the downloaded folder in the terminal with the following commands: "cd url-short"
2. Run the program: "python3 main.py"

You will be prompted with options:
's' - shorten a link
'c' - check how many links were shortened
'o' - enter the shortened link to see the original
'q' - quit the program

## Project Structure
url-short/
|- main.py
|- url.json
|- README.md



