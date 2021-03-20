import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/tsla'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

#Getting stock company name
company_name = soup.find('h1', class_='company__name').text


#Getting stock ticker
stock_ticker = soup.find('span', class_='company__ticker').text

#Getting stock current price
stock_current_price =  soup.find('bg-quote', class_='value').text

#Getting stock last price
stock_last_price = soup.find('td', class_='table__cell u-semi').text

#Gettign stock 52 week range

#First need to get the nested html, so it is easier to get only the information
#that we need
nested_range = soup.find('mw-rangebar', class_='element element--range range--yearly')

stock_range = nested_range.find_all('span', class_='primary')

lower_range = stock_range[0].text
higher_range = stock_range[1].text

#Getting the stock recommendation
recommendation = soup.find('li', class_='analyst__option active').text

#Creating a table
table = pd.DataFrame({'Company':[company_name], 'Ticker':[stock_ticker],
                     'Current Price':[stock_current_price], 'Last Price':[stock_last_price],
                     '52 Weeks Range (lower)':[lower_range],
                     '52 Weeks Range (higher)':[higher_range], 'Recommendation':[recommendation]})
