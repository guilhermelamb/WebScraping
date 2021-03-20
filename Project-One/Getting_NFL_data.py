import pandas as pd
import requests
from bs4 import BeautifulSoup

#Getting link
url = 'https://www.nfl.com/standings/league/2019/PRE'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

#Getting nested table
table = soup.find('table', class_="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")

#Getting headers
headers = []
for header in table.find_all('th'):
    headers.append(header.text)
    for i in range(len(headers)):
        headers[i] = headers[i].strip()
        
#Creating dataframe
df = pd.DataFrame(columns = headers)

#Getting data
table_rows = table.find_all('tr')[1:]

for i in table_rows:
    row_data = i.find_all('td')
    row = [data.text.strip().split('\n')[0] for data in row_data]
    length = len(df)
    df.loc[length] = row

