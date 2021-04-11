from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Initializing driver
driver = webdriver.Chrome('chromedriver.exe')

#Getting the webpage
driver.get('https://www.google.com/')

#Making the search
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 movies of all time imdb')
box.send_keys(Keys.ENTER)

#Cliking in the result
result = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div/div[1]/a')
result.click()

#Waiting some time
time.sleep(10)

#Scrolling to the botton of the page
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

#Taking a screenshot
driver.save_screenshot('page_screenshot.png')

#Taking a screenshot of the poster
driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div[50]/div[2]/a/img').screenshot('50th poster.png')




