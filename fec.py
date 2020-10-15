from bs4 import BeautifulSoup
import requests
import re

def download():
	
	url = 'https://www.fec.gov/data/browse-data/?tab=bulk-data' # bulk download url from FEC website
	s_url = 'https://www.fec.gov' # short url
	res = requests.get(url) # request command
	soup = BeautifulSoup(res.content, 'lxml') #
	loop = soup.find_all('a')
	p = re.compile('/files/bulk-downloads/\d+\Woppexp\d+\Wzip')

	links = []
	for i in loop:
	    if 'files/bulk-downloads' in str(i):
	        dict = {}
	        dict = i['href']
	        links.append(dict)

	files = [i for i in links if p.match(i)]
	files = [s_url+i for i in files]
	filenames = [i[-12:] for i in files]

	for i in range(len(filenames)):
	    r =requests.get(files[i])
	    with open(filenames[i], 'wb') as f:
	        f.write(r.content)

if __name__=="__main__":
	download()


	