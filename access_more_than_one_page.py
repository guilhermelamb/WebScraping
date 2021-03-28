import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.airbnb.com.br/s/Ingleses-Norte--Florian%C3%B3polis-~-SC/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Ingleses%20Norte%2C%20Florian%C3%B3polis%20-%20SC&place_id=ChIJNXMZrQdCJ5UR3iB60zqW4uM&checkin=2021-04-19&checkout=2021-04-30&source=structured_search_input_header&search_type=autocomplete_click'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame(columns=['Title', 'Price', 'Rating', 'Comments', 'Details',
                           'Link'])

#We put the code here into a while loop so until there is a next button
#the loop will gobe true
while True:
        
    postings = soup.find_all('div', class_ = '_8ssblpx')
    
    current_page = soup.find('button', class_='_15k0tg7v').text
    print('Current page: ' + current_page)
    
    #To get the information of every post
    for post in postings:
      
        try:
            #get the link for the posting
            link = post.find('meta', {'itemprop': 'url'}).get('content')
            
            #get the title
            title = post.find('a', class_='_gjfol0').get('aria-label')
            
            #get the price
            price = post.find('span', class_='_olc9rf0').text
            price = int(price[2:])
            
            #get the rating and comments
            rating = post.find('span', class_='_10fy1f8').text
            comments = post.find_all('span', class_='_a7a5sx')[0].text
            comments = re.findall(r'\d+', comments)
            n = [str(i) for i in comments]
            comments = int(''.join(n))
            
            #get the details
            details1 = post.find_all('div', class_='_kqh46o')[0].text
            details2 = post.find_all('div', class_='_kqh46o')[1].text
            
            details = details1 + ' / ' + details2
            
            df = df.append({'Title':title, 'Price':price, 'Rating':rating, 'Comments':comments,
                    'Details':details, 'Link':link}, ignore_index = True)
        except:
            pass
        
        
    #To get the link for the next page
    next_page = soup.find('a', {'aria-label':'Próximo'}).get('href')
    
    #The code above will only a part of the link for the next page, in order to
    #actually go to the next page, we need to add 'https://www.airbnb.com.br/' before
    #Some website will have this form of link but some will have the full link
    
    next_page_full = 'https://www.airbnb.com.br/' + next_page
    
    
    
    #going to the next page
    url = next_page_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
    print('\ngoing to the next page...')


