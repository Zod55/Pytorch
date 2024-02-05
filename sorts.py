from selenium import webdriver
from selenium.webdriver.common.key import Keys
import time 
link =""
driver = webdriver.Chrome()

driver.get()

# find the html to insert the link from the db
insert_element = driver.find_element()
# insert the link of the video and pressing enter
insert_element.send_keys(link)
insert_element.send_keys(Keys.RETURN)

# wait 10
time.sleep(600)