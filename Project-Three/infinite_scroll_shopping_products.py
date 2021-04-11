import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver


#Loading driver
driver = webdriver.Chrome(r'C:\Users\Guilherme\WebScraping\Selenium\chromedriver.exe')

#Getting the webpage
driver.get('https://www.nike.com.br/todos/produtos/ver-lista?p=1&Fabricante=&Filtros=&cor=&tamanho=&precode=&precoate=&ofertas=sim&ordenacao=0&limit=24&ordemFiltro=&site_id=')

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
product_card = soup.find_all('div', class_='produto')

#Creating dataframe
df = pd.DataFrame(columns=['Name', 'Description', 'Old Price', 'Discount Price',\
                           'Link'])

#looping thru all products
for product in product_card:
    try:
        #getting the name of the product
        product_name = product.find('a', class_='produto__nome').text
        
        #getting product old price
        price_old = product.find('span', class_='produto__preco--desabilitado ws-nr').text
        price_old = float(price_old.split(' ')[1].replace('.','').replace(',','.'))
        #getting product discount price
        price_discount = product.find('span', class_='produto__preco_por ws-nr').text
        price_discount = float(price_discount.split(' ')[1].replace('.','').replace(',','.'))
        #getting product short description
        description = product.find('a', class_='produto__descricaocurta').text
        
        #getting the link to the product
        link = product.find('a', class_='produto__nome').get('href')
        
        #appending to the df
        df = df.append({'Name':product_name, 'Description':description, 'Old Price':price_old,\
                        'Discount Price':price_discount, 'Link':link}, ignore_index=True)
    except:
        pass

df['Discount Amount'] = df['Old Price'] - df['Discount Price']








