import urllib.request
import urllib.parse

url = 'https://www.wikipedia.org/'
values = {'search':'new tech',
		  'go':'Go'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)