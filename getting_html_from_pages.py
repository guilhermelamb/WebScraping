import requests
from bs4 import BeautifulSoup

#getting the url
url = "https://webscraper.io/test-sites/e-commerce/allinone"
page = requests.get(url)

#getting the html from the page and parsing with lxml
soup = BeautifulSoup(page.text, 'lxml')

print(soup)