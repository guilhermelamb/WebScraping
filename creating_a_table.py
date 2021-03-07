import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

#Getting all products name
product_name = soup.find_all('a', class_ = 'title')

#Getting price
prices = soup.find_all('h4', class_ = 'pull-right price')

#Getting reviews
reviews = soup.find_all('p', class_ = 'pull-right')

#Getting description
descriptions = soup.find_all('p', class_ = 'description')


#Getting only the text for products, prices, reviews and descriptions

#First, create empty lists
product_name_clean = []
prices_clean = []
reviews_clean = []
descriptions_clean = []

#Now insiade a for loop, use the .text method to get only the text
for i in product_name:
    name = i.text
    product_name_clean.append(name)
    
for i in prices:
    price = i.text
    prices_clean.append(price)

for i in reviews:
    review = i.text
    reviews_clean.append(review)
    
for i in descriptions:
    description = i.text
    descriptions_clean.append(description)
    

table = pd.DataFrame({'Product':product_name_clean, 'Price':prices_clean,
                      'Description':descriptions_clean, 'Reviews':reviews_clean})
    
