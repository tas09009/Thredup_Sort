import requests, urllib.request, time
from bs4 import BeautifulSoup


# OBJECTIVE
# Download NY MTA turnstile data (text files) to local drive.
# Example of data file: <a href="data/nyct/turnstile/turnstile_190831.txt">Saturday, August 31, 2019</a>
# website tutorial: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460


# Set the URL that you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'


# Connect to URL
response = requests.get(url)


# Represents the document as a nested data structure, much nicer and systematic to look at
soup = BeautifulSoup(response.text, "html.parser")


# Pulling text files from line 36-38 (to save time)
for i in range(36,38):
	one_a_tag = soup.findAll('a')[i] # find all the 'a' tags
	link = one_a_tag['href'] # pull all 'href' data within 'a' tags
	download_url = 'http://web.mta.info/developers/' + link # combine the links to pull data from
	urllib.request.urlretrieve(download_url,'./' + link[link.find('/turnstile_') + 1:]) # Download to computer as file name: “turnstile_180922.txt”, “turnstile_180901”, etc.
	time.sleep(1) # pause the code for 1 second
		
