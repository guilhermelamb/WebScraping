import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')

#Checking if it got all boxes
len(boxes)
