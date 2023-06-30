# This program is designed to retrieve a web page specified by the user, parse its HTML content using BeautifulSoup, extract specific data (in this case, the contents of the 'span' tags), convert the extracted data to integers, calculate their sum, and display the final sum. The purpose of the program is to demonstrate web scraping and data extraction from a web page.

from urllib.request import urlopen  # Import the urlopen function from the urllib.request module
from bs4 import BeautifulSoup  # Import the BeautifulSoup class from the bs4 module
import ssl  # Import the ssl module

# Ignore SSL certificate errors
ctx = ssl.create_default_context()  # Create a default SSL context
ctx.check_hostname = False  # Disable hostname checking
ctx.verify_mode = ssl.CERT_NONE  # Disable certificate verification

url = input('Enter - ')  # Prompt the user to enter a URL
html = urlopen(url, context=ctx).read()  # Open the URL and read the HTML content
soup = BeautifulSoup(html, "html.parser")  # Create a BeautifulSoup object for parsing the HTML

# Retrieve all of the anchor tags
tags = soup('span')  # Find all 'span' tags in the HTML
lst = list()  # Initialize an empty list to store data

for tag in tags:  # Iterate over each 'span' tag
    sum = sum + int(tag.contents[0])  # Extract the content of the tag and convert it to an integer, then add it to the running sum

print(sum)  # Print the final sum of all the extracted values
