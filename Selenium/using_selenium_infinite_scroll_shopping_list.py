import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver


#Loading driver
driver = webdriver.Chrome('chromedriver.exe')

#Getting the webpage
driver.get('https://store.unionlosangeles.com/collections/outerwear')

time.sleep(5)

#Initial height
last_height = driver.execute_script('return document.body.scrollHeight')


#Scroll to the botton of the page
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

#Getting the html of the page
soup = BeautifulSoup(driver.page_source, 'lxml')

#Getting the products
product_card = soup.find('div', {'id':'main', 'role':'main'})

postings = product_card.find_all('li')
#Creating dataframe
df = pd.DataFrame(columns=['Designer', 'Description', 'Price', 'Link'])

#looping thru all products
for product in postings:
    try:
        #getting the name of the product
        designer_name = product.find(class_='cap-vendor').text
        
        #getting product old price
        price = product.find(class_='cap-price').text
        price = float(price.split('$')[1].replace(',','').replace('.',','))
        
        #getting product short description
        description = product.find(class_='cap-title').text
        
        #getting the link to the product
        link = product.find('a').get('href')
        link = 'https://store.unionlosangeles.com'+link
        #appending to the df
        df = df.append({'Designer':designer_name, 'Description':description, 'Price':price,\
                        'Link':link}, ignore_index=True)
    except:
        pass












