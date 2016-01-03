import urllib
import request
url = 'http://10.24.35.228:8000/favicon.ico'
headers = {'xxxx'}
request = urllib.Request(url,headers = headers)
response = urllib.urlopen(request)
print (response.read())