import pandas as pd
import requests
from bs4 import BeautifulSoup

#Get link
url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

#Getting nested table
table = soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')


#Headers
headers = []
table_headers = table.find_all('th')

for i in table_headers:
    headers.append(i.text)
    
    
#Creating dataframe
df = pd.DataFrame(columns = headers) 

   
#Get the data
table_rows = table.find_all('tr')[1:]

for i in table_rows:
    row_data = i.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row
  

