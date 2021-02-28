import requests
from bs4 import BeautifulSoup

#getting the url
url = "https://webscraper.io/test-sites/e-commerce/allinone"
page = requests.get(url)

#getting the html from the page and parsing with lxml
soup = BeautifulSoup(page.text, 'lxml')


#accessing tags
header = soup.header
#print(header)

body = soup.body
#print(body)

#getting the content of a tag
tag = soup.header.a

#this will show all atributes for this tag in a dictionary
tag.attrs

#look for a spacific attribute
tag['data-toggle']


