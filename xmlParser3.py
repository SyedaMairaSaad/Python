#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#py get-pip.py
#py -m pip help
#pip install beautifulsoup4cd 
import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
import ssl
#ignore ssl certificate errrors
ctx=ssl.create_default_context()
ctx.check_hostname=ssl.CERT_NONE

url=input('Enter- ')
#url='http://py4e-data.dr-chuck.net/comments_42.html'
xml=urllib.request.urlopen(url,context=ctx).read()
xmlParse=ET.fromstring(xml)
dataTree=xmlParse.findall('comments/comment')
print('Retrieved',len(xml),'characters')
print('Count:',len(dataTree))

sum=0
for tree in dataTree:
    c=tree.find('count').text
    sum=sum+int(c)
print('Sum:',sum)

