import pandas as pd
import requests
from bs4 import BeautifulSoup

#Getting the url
url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)
print(page)


#Getting the data
soup = BeautifulSoup(page.text, 'lxml')
print(soup)

table_data = soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')

headers = []
for i in table_data.find_all('th'):
    title = i.text
    headers.append(title)
    
print(headers)

#Transforming the data into a dataframe
df = pd.DataFrame(columns = headers)

for i in table_data.find_all('tr')[1:]:
    row_data = i.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row
    
    
