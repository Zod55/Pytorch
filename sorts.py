from selenium import webdriver
from selenium.webdriver.common.key import Keys
from bs4 import BueatifulSoup as bs
import time 
import requesta
def get_account(): 
  email_html = requests.get("https://internxt.com/temporary-email")
  if email_html == 200:
     soup_email =bs(email_html.contact, 'html.preser')
     rmemail = bs.find("p", _class="flex h-full w-full cursor-pointer flex-row items-center justify-between rounded-xl bg-gray-1 shadow-sm  px-4 py-3")



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


def create_short():
   with open("file.xlm","r") as f:
     



    # wait 10
    time.sleep(600)
