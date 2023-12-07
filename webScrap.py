#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#py get-pip.py
#py -m pip help
#pip install beautifulsoup4cd 
import urllib.request,urllib.parse,urllib.error

from bs4 import BeautifulSoup
import ssl
def get_url(url):
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    #tags=
    return soup('a')
#ignore ssl certificate errrors
ctx=ssl.create_default_context()
ctx.check_hostname=ssl.CERT_NONE

url=input('Enter- ')
#url='http://py4e-data.dr-chuck.net/comments_42.html'
tags=get_url(url)
count=input('Enter count:')
countran=0
pos=input('Position-')
for i in range(0,int(count)+1):
    print('Retrieving:',url)
    url=tags[int(pos)-1].get('href',None)   
    #print('get:',url)
    tags=get_url(url)

    

    
            
            
            
            
            
        

    

        