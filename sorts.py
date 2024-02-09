from selenium import webdriver
from selenium.webdriver.common.key import Keys
from bs4 import BueatifulSoup as bs
import time 
import requests
import openpyxl


def get_account(): 
  email_html = requests.get("https://internxt.com/temporary-email")
  if email_html == 200:
     soup_email =bs(email_html.contact, 'html.preser')
     rmemail = bs.find("p", _class="flex h-full w-full cursor-pointer flex-row items-center justify-between rounded-xl bg-gray-1 shadow-sm  px-4 py-3")

"""
1. need to put the drive in global variable 
2. add therads so we have multiple chrome tabs
3. add a function to download the 3 first file
3. add a function that will upload the file through
the YouTube api 
4. add a function that will put a video under the downloaded 
video 
"""

#need to put the path to chrome find it later 
  driver = webdriver.Chrome()
#need to put the link to the rendom email website 
  driver.get()

# find the html to insert the link from the db
  insert_email = driver.find_element(_class="supabase-auth-ui_ui-input !rounded-xl c-dEnagJ c-dEnagJ-bBzSYw-type-default")
  insert_pass = driver.find_element(_class="supabase-auth-ui_ui-input !rounded-xl c-dEnagJ c-dEnagJ-bBzSYw-type-password")

# insert the rendom email and pressing enter
  insert_email.send_keys(rmemail)
  insert_pass.send_keys("123456789")
  insert_element.send_keys(Keys.RETURN)
  #need to add a code that will press the link on 
  #the random email address website 

def create_short(catgeroy):
     #open the excel 
     workbook = openpyxl.load_workbook('my_file.xlsx')
     #select the active sheet
     sheet = workbook.active
     for cell in sheet[catagory]:
          insert_email = driver.find_element("""need to put the class for insert the link""")
        
          



    # wait 10
    time.sleep(600)














# Iterate over the cells in the first column and append data to the array
for cell in sheet['A']:
    data_array.append(cell.value)

# Print the data array to see the result
print(data_array)