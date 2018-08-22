from bs4 import BeautifulSoup
import requests
import csv

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

url = requests.get('https://www.reddit.com/r/todayilearned/', headers=headers)
urlContent =BeautifulSoup(url.content,"lxml")

csvFile = open('TIL.csv', 'w')
csvWrite = csv.writer(csvFile)
csvWrite.writerow(['Today I Learned'])

for headings in urlContent.find_all('h2'):
	headings = headings.text
	print(headings)	
	print()
	csvWrite.writerow([headings])

csvFile.close()