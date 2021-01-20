import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)  # to parse XML that is stored in a string
print('Name:', tree.find('name').text)
print('AttrOne:', tree.find('phone').get('type'))
print('AttrTwo:', tree.find('email').get('hide'))