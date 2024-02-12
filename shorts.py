from selenium import webdriver
from selenium.webdriver.common.key import Keys
from bs4 import BueatifulSoup as bs
import time 
import requests
import openpyxl
import random

#need to put the path to chrome find it later
def random_password(length=12):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined length and character pool
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

driver = webdriver.Chrome()
def download_short(driver):
def get_account(driver): 

 driver.get('https://internxt.com/temporary-email')
 # Find the div of the renemail
rmemail = driver.find_element_by_id('eposta_adres').get_attribute('data-clipboard-text')

# Get the value of the data-clipboard-text attribute
"""
after gatting the massge need to go back to the rm email website and press this button 
button = driver.find_element_by_xpath('//svg[@class="cursor-pointer"]')
need to add code to press the link
"""
 driver.execute_script("window.open('about:blank', '_blank');")
 driver.switch_to.window(driver.window_handles[1])


"""
1. need to put the drive in global variable: done 
2. add therads so we have multiple chrome tabs:
3. add a function to download the 3 first file:
3. add a function that will upload the file through
the YouTube api: 
4. add a function that will put a video under the downloaded 
video:
5. some chages on the create short function need to see how to insert the link for the first time and 
then for all the other and put the limit for the 60 min use 
"""
driver.switch_to.window(driver.window_handles[1])

#we get in the ai shorts website
 driver.get("https://www.veed.io/signup")
# need to press the crate new account
# find the html to insert the new account
 insert_random_name = driver.find_element_by_id("input-188")
 insert_email = driver.find_element_by_id("input-191")
 insert_pass = driver.find_element_by_id("input-194")
 random_pass = random_password() 
# insert the rendom email and pressing enter
 insert_random_name.send_keys(random.randint())
 insert_email.send_keys(rmemail)
 insert_pass.send_keys(random_pass)
 policiy_ok = driver.find_element(_class="v-input--selection-controls__ripple")
 policiy_ok.click()
 driver.fins_element(_class="sign-up__wrapper__form__switch__to__form__button").click()
 #need to add a code that will press the link 
 driver.switch_to.window(driver.window_handles[0])
 email_ver_link = driver.find_element_by_xpath(_class="gonderen")
 email_ver_link.click()
 ver_link = driver.find_element_by_xpath('//a[contains(@href, "app.chopcast.io/verify")]')
 ver_link.click()
 driver.find_element_by_css_selector('button[data-v-ff9cb54e=""]').click()
 driver.find_element_by_class_name("sign-in-form__login__form__submit").click()
 time.sleep(60)


def create_short(catgeroy,driver):
     #open the excel 
     workbook = openpyxl.load_workbook('my_file.xlsx')
     #select the active sheet
     sheet = workbook.active
        # chage some in here
     enter_upload = driver.find_element(_class="v-btn v-btn--disabled v-btn--has-bg theme--light v-size--default")
     for cell in sheet[catagory]:
          driver.find_element_by_id("no-background-hover")click()
          driver.find_element_by_id("list-item-383").click()
          
          upload = driver.find_element(_class="v-btn v-btn--text theme--light v-size--default")
          upload.click()
          language_selector = driver.find_element_by_id("id=input-356")  # Replace "language_selector_id" with the actual ID of your language selector
          language_selector.click()
          language_selector.send_keys(Keys.ARROW_DOWN)
          time.sleep(1)
          language_selector.send_keys(Keys.ENTER)
          insert_link = driver.find_element_by_css_selector('input[data-ddg-inputtype="unknown"]')
      #till here
          insert_link.send_keys(cell.value)
          time.sleep(30)
          download_short(driver)


# Iterate over the cells in the first column and append data to the array
for cell in sheet['A']:
    data_array.append(cell.value)

# Print the data array to see the result
print(data_array)













