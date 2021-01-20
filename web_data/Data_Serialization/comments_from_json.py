import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

comments = []

# https://py4e-data.dr-chuck.net/comments_42.json
# https://py4e-data.dr-chuck.net/comments_1114752.json
url = input('Enter location: ')

print('Retrieving: ', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print(json.dumps(js, indent=4))

for item in js['comments']:
    comments.append(int(item['count']))

print(sum(comments))

