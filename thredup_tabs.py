
# OBJECTIVE
# Filter out clothing items (thredup.com) by removing items with descriptions: "polyester" or "Fabric details not available"

import requests, time, re, pprint, sys, webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver

# Set the URL that you want to webscrape from
url = 'https://www.thredup.com/products/petite?chars_sleeve_length=sleeveless&department_tags=petite&search_tags=women-tops%2Cwomen-tops-blouses&sizing_id=750%2C755&skip_equivalents=true&sort=Newest+First&state=listed'

# Connect to URL
response = requests.get(url)

# Represents the document as a nested data structure, much nicer and systematic to look at
soup = BeautifulSoup(response.text, "html.parser") # <class 'bs4.BeautifulSoup'> # print(soup.prettify()) # class 'str'


# -----------------------------------------------------------------------------------------------
# DEF: pulls out links for each item in a thredup category

list_link = []

def find_link(start,stop):

	for i in range(start,stop):

		# Find all attibutes with "item-card-top" (there will be 1 for each clothing item)
		item_attribute = soup.find_all(attrs={"class": "item-card-top"})[i] # print(type(item_attribute)) # class 'bs4.element.ResultSet'
		
		# find the 1st 'a' tag
		product = item_attribute.find('a')

		# pull all 'href' data within 'a' tags (there is only 1)
		link = product['href']
		
		# combine the links to pull data from
		download_url = 'https://www.thredup.com' + link 

		list_link.append(download_url)

	return list_link # reference for next function

list_link = find_link(9,13)
	
	
# ------------------------------------------------------------------------------------------------------
# DEF: loop through each item in list and pull link if it doesn't contain the "banned" words


def open_link(list_link):
	
	for i in range(len(list_link)): # from 0 to length of list

		url1 = list_link[i]

		response1 = requests.get(url1)

		# Represents the document as a nested data structure, much nicer and systematic to look at
		soup1 = BeautifulSoup(response1.text, "html.parser") # <class 'bs4.BeautifulSoup'>

		# Search for polyester throughout the div tags
		des_attr = soup1.find(attrs={"class": "item-details-detail item-details-materials"}) # print(description2) # class 'bs4.element.ResultSet'
		des_text = des_attr.get_text() # class = string

		# If it contains the "banned" words, print them out. If not, open new tab
		if (des_text.find('Polyester') != -1): 
			print ('Polyester') 
		elif (des_text.find('Fabric details not available') != -1):
			print ('Fabric details not available')
		else: 
			webbrowser.open_new(url1)
			time.sleep(3) # pause the code for 3 seconds

open_link(list_link)














# if des_text.find('polyester'):
# 	print('polyester')
# else:
# 	open_link()

# def open_link():
# 	webbrowser.open_new(response1)
# 	time.sleep(2) # pause the code for 1 second



# Item page with materials description
# def omit():
# list_link1 = []

# pulls out links for each item in a thredup category


# for i in list_link:
# # # Set the URL that you want to webscrape from
# # 	url_omit = list_link[i]
# # 	# print(url_omit)

# 	# Connect to URL
# 	response1 = requests.get(list_link[i])

# 	# Represents the document as a nested data structure, much nicer and systematic to look at
# 	soup = BeautifulSoup(response1.text, "html.parser") # <class 'bs4.BeautifulSoup'>

# 	# Search for polyester through the div tags
# 	for i in list_link:

# 		des_attr = soup.find(attrs={"class": "item-details-detail item-details-materials"})[i] # print(description2) # class 'bs4.element.ResultSet'
# 		des_text = des_attr.get_text()

# 		if des_text.find('polyester'):
# 			print('polyester')
# 		else:
# 			open_link()



# # def open_link():
# for i in list_link:
# 	webbrowser.open_new(i)
# 	time.sleep(3) # pause the code for 1 second


# find_link()
# omit()
# open_link()







# description1 = soup.select('div[class="item-details-detail item-details-materials"]') # <class 'list'>
# description2 = description1.select('strong')


# item = product.select("div > href")
# print(item)


# testing = soup.find_all("div")[0]
# checking = soup.find_all("div").attrs
# print(checking)





# for link in soup.find_all('a'):
#     links = link.get('href')
# download_url = 'https://www.thredup.com/' + links # combine the links to pull data from
# print(download_url) # <class 'str'>



# one_a_tag = soup.findAll('a') # find all the 'a' tags
# link = one_a_tag['href'] # pull all 'href' data within 'a' tags
# # list_link = list(link)
# download_url = 'https://www.thredup.com/' + link # combine the links to pull data from
# print(download_url) # <class 'str'>


	
# download_url = 'https://www.thredup.com/' + link # combine the links to pull data from


# Starting from line 389 (in increments of 3), open each link in a new tab

# Unless it contains the word "polyester" in the description

# Discription of item: html code of line ______ (fabric line)






# one_a_tag = soup.findAll('a') # find all the 'a' tags
# class 'bs4.element.ResultSet'



# link to category search: https://www.thredup.com/products/petite?chars_sleeve_length=sleeveless&department_tags=petite&search_tags=women-tops%2Cwomen-tops-blouses&sizing_id=750%2C755&skip_equivalents=true&sort=Newest+First&state=listed
# link to product: <a href="/product/women-ann-taylor-loft-purple-sleeveless-blouse/60288429?sizing_id=750%2C755"><div class="item-title">Sleeveless Blouse</div><div class="size-name">Size XXS (Petite)</div><div class="price-line"><div class="formatted-prices"><span class="formatted-price price-color--regular"><!-- react-text: 25272 -->$<!-- /react-text --><!-- react-text: 25273 -->18.99<!-- /react-text --></span><span class="formatted-msrp"><!-- react-text: 25275 -->$<!-- /react-text --><!-- react-text: 25276 -->55<!-- /react-text --></span></div><button aria-label="Add to Cart" class="_2qc0J js-modal-trigger-atc" type="button">Add to Cart</button></div></a>
