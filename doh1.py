from selenium import webdriver
from selenium.webdriver.common.key import Keys
import time


driver = webdriver.Chrome()
driver.get('https://one.prat.idf.il/login') 

insert_id = driver.find_element(_class ="formControl")
insert_id.send_keys(input("whats your id:"))
insert_id.send_keys(Keys.RETURN)

insert_pass = driver.find_element(_class="form-control input ext-input text-box ext-text-box")
inert_pass = driver.send_keys(input("whats yout pass")
insert_pass.send_keys(Keys.RETURN)
"""
1. need to see how we get in to the microsoft and take the code from the mail
2. add the press the doh1
3. send the like to the group chat
"""
