import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.carpages.ca/used-cars/search/?category_id=5'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame(columns = ['Name', 'Year', 'Price', 'Mileage', 'Color', 'Link'])

page_number = 1

max_pages = 15

while page_number <= max_pages:
    
    print('Current page: {}'.format(page_number))
    
    posting = soup.find_all('div', class_='media soft push-none rule')
    
    for post in posting:
        
        try:
            #Getting the name year of the car
            name = post.find('h4', class_='hN').text
            year = name[:5]
            name = name[5:].strip()
            
            #Getting the link for the post
            link = post.find('a').get('href')
            full_link = 'https://carpages.ca' + link
            
            #Getting the price
            price = post.find('strong', class_='delta').text.strip()
            
            #Getting the mileage
            mileage = post.find_all('div', class_='grey l-column l-column--small-6 l-column--medium-4')[0].text

            #Getting the color
            color = post.find_all('div', class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
            
            #Appending the data to the dataframe
            df = df.append({'Name':name, 'Year':year, 'Price':price, 'Mileage':mileage,
                            'Color':color, 'Link':full_link}, ignore_index = True)
        except:
            pass
        

    #Finding the link for the next page
    next_page = soup.find('a', class_='nextprev').get('href')
    
    #Repeating the process with the new link
    url = next_page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
    print('\nGoing to the next page...')
    
    page_number += 1
