from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com/')

#Entering text into the search box
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('cute puppies')
box.send_keys(Keys.ENTER)

#Clicking in the images button
button = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
button.click()

#Self-scrolling

#This method gets the height of the web page, but if we keep scrolling down
#this height will increase
driver.execute_script('return document.body.scrollHeight')


#This method goes to a specific height of the page
driver.execute_script('window.scrollTo(0, 2000)')

#We can combine these two to go to the botton of the page

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')