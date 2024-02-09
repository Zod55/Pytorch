from selenium import webdriver
from selenium.webdriver.common.key import Keys
from bs4 import BueatifulSoup as bs
import time 
import requests
import openpyxl


#need to put the path to chrome find it later 
driver = webdriver.Chrome()

def get_account(): 

 driver.get('https://internxt.com/temporary-email')
 # Find the div of the renemail
 rmemaildiv = driver.find_element_by_xpath('//div[contains(@class, "flex") and contains(@class, "h-full") and contains(@class, "w-full") and contains(@class, "cursor-pointer") and contains(@class, "flex-row") and contains(@class, "items-center") and contains(@class, "justify-between") and contains(@class, "rounded-xl") and contains(@class, "bg-gray-1") and contains(@class, "shadow-sm") and contains(@class, "px-4") and contains(@class, "py-3")]')
# Find the rmemail on the website
 rmemail = parent_div.find_element_by_tag_name('p').text

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
"""

#we get in the ai shorts website
 driver.get("https://klap.app/login")

# find the html to insert the link from the db
 insert_email = driver.find_element(_class="supabase-auth-ui_ui-input !rounded-xl c-dEnagJ c-dEnagJ-bBzSYw-type-default")
 insert_pass = driver.find_element(_class="supabase-auth-ui_ui-input !rounded-xl c-dEnagJ c-dEnagJ-bBzSYw-type-password")

# insert the rendom email and pressing enter
 insert_email.send_keys(rmemail)
 insert_pass.send_keys("123456789")
 insert_element.send_keys(Keys.RETURN)
 #need to add a code that will press the link on 
 driver.get('https://shorts-with-ai.com')
 
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



# Open the first tab and navigate to the email service
driver.get('https://your-email-service.com')

# Open a new tab

# Switch to the second tab
driver.switch_to.window(driver.window_handles[1])

# Navigate to the website that creates shorts with AI

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])

# Now you are back to the first tab










# Iterate over the cells in the first column and append data to the array
for cell in sheet['A']:
    data_array.append(cell.value)

# Print the data array to see the result
print(data_array)












# Open a webpage
driver.get('https://example.com')

# Find the parent div element
parent_div = driver.find_element_by_xpath('//div[@class="parent-class"]')

# Find the <p> element inside the parent div
p_element = parent_div.find_element_by_tag_name('p')

# Extract the text from the <p> element
text = p_element.text

# Print the extracted text
print(text)

# Close the WebDriver
driver.quit()
