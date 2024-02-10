from selenium import webdriver
from selenium.webdriver.common.key import Keys
import time


driver = webdriver.Chrome()
driver.get('https://one.prat.idf.il/login') 

insert_id = driver.find_element(_class ="formControl")
insert_id.send_keys(input("whats your id:"))
insert_id.send_keys(Keys.
