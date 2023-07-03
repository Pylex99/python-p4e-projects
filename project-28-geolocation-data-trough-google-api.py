# The purpose of this program is to retrieve geolocation data for a given address using either the py4e-data API or the Google Maps API. It prompts the user to enter an address, constructs a request URL with the address as a parameter, and sends an HTTP request to the API service. The program then retrieves the response, parses the JSON data, and extracts relevant information such as the formatted address and country code. Finally, it displays the retrieved data, including the formatted address and the two-letter country code.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'  # Service URL for py4e-data API
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'  # Service URL for Google Maps API

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)  # Construct the complete URL with parameters

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)  # Open the URL with SSL context
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)  # Parse the JSON response into a Python object
    except:
        js = None

    # Check if the JSON response is valid and contains the expected status
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))  # Print the formatted JSON response

    location = js['results'][0]['formatted_address']
    try:
        country = location.split()[3]  # Extract the country from the formatted address
        country = country[:2]  # Take the first two characters of the country name
        print(country)
    except:
        print("No COUNTRY")
    #country = location[]
    #print(location)