
import urllib.request,urllib.parse,urllib.error
import json


import ssl
#ignore ssl certificate errrors
ctx=ssl.create_default_context()
ctx.check_hostname=ssl.CERT_NONE

#url=input('Enter- ')
url='https://py4e-data.dr-chuck.net/comments_1941001.json'
uh=urllib.request.urlopen(url)
data=uh.read().decode()
print('Retrieved',len(data),'characters')
try:
    js=json.loads(data)
except:
    js=None
        

comments=js['comments']
print('Count',len(comments))
count=0
for i in range(0,len(comments)):
    count=count+comments[i]['count']
print('Sum',count)