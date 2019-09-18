


# OBJECTIVE
# Download NY MTA turnstile data (text files) to local drive.
# Example of data file: <a href="data/nyct/turnstile/turnstile_190831.txt">Saturday, August 31, 2019</a>

import requests, urllib.request, time, re, pprint, sys, webbrowser
from bs4 import BeautifulSoup



# Set the URL that you want to webscrape from
url = 'https://www.thredup.com/products/petite?chars_sleeve_length=short+sleeve&department_tags=petite&search_tags=women-tops%2Cwomen-tops-button-down-shirts&sizing_id=750%2C755%2C756%2C765&skip_equivalents=true&state=listed'


# Connect to URL
response = requests.get(url)


# Represents the document as a nested data structure, much nicer and systematic to look at
soup = BeautifulSoup(response.text, "html.parser") # <class 'bs4.BeautifulSoup'>
# print(soup.prettify()) # class 'str'




# item_attribute = soup.find_all(attrs={"class": "item-card-top"})

css_select = '#js-shop-app-root > div:nth-child(2) > div.mobile-nav-content-close > main > div.u-flex > section > div.hD2uz > div.results-grid > div:nth-child(1) > div > div.item-card-top > a'


item_attribute = soup.select(css_select)

# print(item_attribute.prettify()) # class 'bs4.element.Tag'
# print(type(item_attribute)) # class 'bs4.element.ResultSet'


# find the 1st 'a' tag
# product = item_attribute.find('a')

print(item_attribute)