# The purpose of this program is to retrieve data from a JSON API, specifically comments and their counts, and then calculate and display the total count of comments as well as the sum of all comment counts. The user is prompted to enter a URL, and if no input is provided, a default URL is used.

import urllib.request
import json

while True:
    url = input('Enter url: ')
    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/comments_1665623.json"  # Default URL if no input is provided
    else:
        url = "Done"
        break  # Exit the loop if "Done" is entered as the input

    url_handle = urllib.request.urlopen(url)  # Open the URL
    data = url_handle.read()  # Read the contents of the URL
    #print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)  # Parse the JSON data
    except:
        js = None

    count = 0
    lst = list()
    for comment in js["comments"]:
        count += 1  # Count the number of comments
        lst.append(comment["count"])  # Append the count of each comment to the list

    print("count:", count)  # Print the total count of comments
    print(sum(lst))  # Print the sum of all comment counts

