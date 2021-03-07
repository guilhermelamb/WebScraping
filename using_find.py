import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

#Find -> used to search and filter for specific text
#First, we put the tag we are looking for and then the attribute

test_find = soup.find('div', {'class':'container test-site'})

#So we only get content from this specific div tag
print(test_find)

test_find_price = soup.find('h4', {'class':'pull-right price'})
print(test_find_price)

#For the class attribute we can do the following way

test_class = soup.find('h4', class_ = 'pull-right price')
print(test_class)