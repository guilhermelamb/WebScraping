import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#The person you want to get the most recent tweets
print("Please, write the name of the profile:\n")
person = str(input())

#getting driver and web page
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://twitter.com/login')

#Time to wait until the page fully load
time.sleep(2)


#Entering login
login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
login.send_keys('######') #here you have to use your login


#Entering password
password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys('######') #here you have to use your passward

button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
button.click()

#Wait until searchbar loads
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')))

#Using searchbar
search = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
search.send_keys(person)
search.send_keys(Keys.ENTER)

#Go to people tab
people = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[3]')
people.click()

#Wait some time for the page to load
time.sleep(2)

#Go to the profile
profile = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span')
profile.click()

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'lxml')

#Getting the postings
postings = soup.find_all('div', class_='css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')

tweets =[]

while True:
    for post in postings:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_='css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    unique_tweets = list(set(tweets))
    if len(unique_tweets) > 200:
        break

#If you want to search for a specific word in the tweets
tweets_subset = []
for i in unique_tweets:
    if 'gym' in i: #just change the word 'gym' to whatever you want
        tweets_subset.append(i)
        