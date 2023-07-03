# The purpose of this program is to allow the user to enter a location, retrieve the geographical coordinates (latitude and longitude), and display the formatted address of that location. The code handles the API request, parses the JSON response, and extracts the necessary information from it. It also includes error handling in case the request fails or the response is not in the expected format.

import urllib.request, urllib.parse, urllib.error
import json

api_key = False

# Check if an API key is provided; if not, use a default key or service URL
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'  # Service URL for py4e-data API
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'  # Service URL for Google Maps API

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
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)  # Parse the JSON response into a Python object
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))  # Print the formatted JSON response

    # Extract the latitude, longitude, and formatted address from the JSON response
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
