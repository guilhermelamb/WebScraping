from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com/')


#Entering text into the search box
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('cute puppies')
box.send_keys(Keys.ENTER)


#here it will wait 10 seconds to see if it finds the ID 'cnt', if this ID isn't
#find, it will raise an error and the code will stop running
#if the ID is found quickly, it won't wait the 10s
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cnt')))

#Time is used to wait some time before doing the next action
#time in seconds, here 10 seconds
time.sleep(10)

#Clicking in the images button
button = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
button.click()


