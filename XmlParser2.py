import xml.etree.ElementTree as ET
data='''<staff>
<users>
<user>
<name>Maira</name>
<telephone type="intl">+12345</telephone>
<email hide="Yes"/>
</user>
<user>
<name>Ali</name>
<telephone type="intl">+12346</telephone>
<email hide="No"/>
</user>
</users>
</staff>'''

xmlData=ET.fromstring(data)
dataTree=xmlData.findall("users/user")
print("Count:",len(dataTree))
for tree in dataTree:
    print("Name:",tree.find("name").text)
    print("Email:",tree.find("email").get("hide"))