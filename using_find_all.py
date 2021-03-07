import requests
from bs4 import BeautifulSoup
import re

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

soup.find_all('h4', {'class':'pull-right price'})


soup.find_all('a', class_ = 'title')


#Return more than one tag

soup.find_all(['h4', 'p'])

#We can return all tags that have an id
soup.find_all(id = True)

#Search based on a string
soup.find_all(string = 'Iphone')

soup.find_all(string = ['Iphone', 'Nokia 123'])

#Using re
soup.find_all(string = re.compile('Iph'))

soup.find_all(string = re.compile('Nokia'))

#Can also search for classes that have specific text
soup.find_all(class_ = re.compile('pull'))

soup.find_all('p', class_ = re.compile('pull'))

#We can also limit the results
soup.find_all('p', class_ = re.compile('pull'), limit = 3)
