#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#py get-pip.py
#py -m pip help
#pip install beautifulsoup4cd 
import urllib.request,urllib.parse,urllib.error

from bs4 import BeautifulSoup
import ssl
#ignore ssl certificate errrors
ctx=ssl.create_default_context()
ctx.check_hostname=ssl.CERT_NONE

url=input('Enter- ')
#url='http://py4e-data.dr-chuck.net/comments_42.html'
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
count=0
sum=0
for tag in tags:
    count=count+1
    sum=sum+int(tag.contents[0])
print('Count',count)
print('Sum',sum)
    