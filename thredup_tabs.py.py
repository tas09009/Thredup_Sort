# import webbrowser
# webbrowser.open('https://www.thredup.com/')

import requests, urllib.request, time, re
from bs4 import BeautifulSoup


# OBJECTIVE
# Download NY MTA turnstile data (text files) to local drive.
# Example of data file: <a href="data/nyct/turnstile/turnstile_190831.txt">Saturday, August 31, 2019</a>


# Set the URL that you want to webscrape from
url = 'https://www.thredup.com/products/petite?chars_sleeve_length=sleeveless&department_tags=petite&search_tags=women-tops%2Cwomen-tops-blouses&sizing_id=750%2C755&skip_equivalents=true&sort=Newest+First&state=listed'


# Connect to URL
response = requests.get(url)


# Represents the document as a nested data structure, much nicer and systematic to look at
soup = BeautifulSoup(response.text, "html.parser") # <class 'bs4.BeautifulSoup'>
print(type(soup))
# print(soup.prettify())
# class 'str'



# one_a_tag = soup.findAll('a') # find all the 'a' tags
# class 'bs4.element.ResultSet'









# link to category search: https://www.thredup.com/products/petite?chars_sleeve_length=sleeveless&department_tags=petite&search_tags=women-tops%2Cwomen-tops-blouses&sizing_id=750%2C755&skip_equivalents=true&sort=Newest+First&state=listed
# link to product: <a href="/product/women-ann-taylor-loft-purple-sleeveless-blouse/60288429?sizing_id=750%2C755"><div class="item-title">Sleeveless Blouse</div><div class="size-name">Size XXS (Petite)</div><div class="price-line"><div class="formatted-prices"><span class="formatted-price price-color--regular"><!-- react-text: 25272 -->$<!-- /react-text --><!-- react-text: 25273 -->18.99<!-- /react-text --></span><span class="formatted-msrp"><!-- react-text: 25275 -->$<!-- /react-text --><!-- react-text: 25276 -->55<!-- /react-text --></span></div><button aria-label="Add to Cart" class="_2qc0J js-modal-trigger-atc" type="button">Add to Cart</button></div></a>