# The purpose of this program is to retrieve an XML document from a specified URL, parse the XML using ElementTree, extract specific data from the XML (in this case, the 'count' values within 'comment' elements), calculate their sum, and display the count and sum on the console.

import urllib.request, urllib.parse, urllib.error  # Import necessary modules from urllib library
import xml.etree.ElementTree as ET  # Import the ElementTree module from the xml library

url = input('Enter url: ')  # Prompt the user to enter a URL
print('Retrieving', url)

total = 0  # Initialize a variable to store the total sum
count = 0  # Initialize a variable to count the items

uh = urllib.request.urlopen(url)  # Open the URL
data = uh.read()  # Read the content of the URL
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)  # Create an ElementTree object from the XML content
lst = tree.findall('comments/comment')  # Find all 'comment' elements in the XML

for item in lst:  # Iterate over each 'comment' element
    count = count + 1  # Increment the count
    t = item.find('count').text  # Find the 'count' element and extract its text content
    total = total + float(t)  # Convert the extracted text to float and add it to the total sum

print('Count:', count)  # Print the count of items
print('Sum:', total)  # Print the total sum
