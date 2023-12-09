import xml.etree.ElementTree as ET
data='''<person>
<name>maira</name>
<telephone type="intl">+12345</telephone>
<email hide="Yes"/>
</person>'''

tree=ET.fromstring(data)
print("Name:",tree.find("name").text)
print("Email:",tree.find("email").get("hide"))