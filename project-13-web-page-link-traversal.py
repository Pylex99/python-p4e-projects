# This program crawls the specified web page and traverses the links on that page.


import urllib.request, urllib.parse, urllib.error  # Import necessary modules from urllib library
from bs4 import BeautifulSoup  # Import the BeautifulSoup class from the bs4 module
import ssl  # Import the ssl module

# Ignore SSL certificate errors
ctx = ssl.create_default_context()  # Create a default SSL context
ctx.check_hostname = False  # Disable hostname checking
ctx.verify_mode = ssl.CERT_NONE  # Disable certificate verification

url = input('Enter - ')  # Prompt the user to enter a URL
html = urllib.request.urlopen(url, context=ctx).read()  # Open the URL and read the HTML content
soup = BeautifulSoup(html, 'html.parser')  # Create a BeautifulSoup object for parsing the HTML

count = int(input("Enter count :"))  # Prompt the user to enter a count value
position = int(input("Enter position :")) - 1  # Prompt the user to enter a position value (adjusted by -1 to match list indexing)
href = soup("a")  # Find all 'a' tags in the HTML and store them in a list
print(href)  # Print the list of 'a' tags

for i in range(count):  # Iterate 'count' number of times
    link = href[position].get('href', None)  # Get the href attribute of the 'a' tag at the specified position
    print(href[position].contents[0])  # Print the contents of the 'a' tag at the specified position
    html = urllib.request.urlopen(link, context=ctx).read()  # Open the URL from the href and read its HTML content
    soup = BeautifulSoup(html, "html.parser")  # Create a new BeautifulSoup object for parsing the new HTML content
    href = soup('a')  # Update the 'href' list with the 'a' tags found in the new HTML
