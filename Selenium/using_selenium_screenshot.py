from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com')

#Pressing 'ENTER'
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('cute puppies')
box.send_keys(Keys.ENTER)

#Clicking in the "images" button
button = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
button.click()

#Taking a screenshot
driver.save_screenshot('puppies.png')

#Taking a screenshot of a specific element
driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').screenshot('specific_puppy.png')

#Here by doing a for loop, we can loop thru several images and take a screenshot
#of each one

for i in range(1,51):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(str(i)))\
        .screenshot('puppy_{}.png'.format(str(i)))
    except:
        next