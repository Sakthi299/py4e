import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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
# https://py4e-data.dr-chuck.net/comments_42.xml
# https://py4e-data.dr-chuck.net/comments_1114751.xml
address = input('Enter location: ')

url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')

for item in lst:
    comments.append(int(item.find('count').text))

print(sum(comments))
