from bs4 import BeautifulSoup
import requests
import re
import shutil

def download():
	
	url = 'https://www.fec.gov/data/browse-data/?tab=bulk-data' # bulk download url from FEC website
	s_url = 'https://www.fec.gov' # short url
	res = requests.get(url) # request command
	soup = BeautifulSoup(res.content, 'lxml') # scrapper
	loop = soup.find_all('a') # look for links
	p = re.compile('/files/bulk-downloads/\d+\Woppexp\d+\Wzip') # use this to regex the files I need

	links = []
	for i in loop:
	    if 'files/bulk-downloads' in str(i):
	        dict = {}
	        dict = i['href'] # extract the links
	        links.append(dict)

	files = [i for i in links if p.match(i)]
	files = [s_url+i for i in files] # links for download
	filenames = [i[-12:] for i in files] # filenames for file saving

	for i in range(len(filenames)):
		r =requests.get(files[i]) # download
		with open(filenames[i], 'wb') as f: # wb ok for zip files
			f.write(r.content) # file save

	for i in range(len(filenames)):
		shutil.move(filenames[i], 'zips') # copying files to folder

# use this so that it'll run in cmd
if __name__=="__main__":
	download()