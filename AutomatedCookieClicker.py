#This is how you automate a cookie clicker game
#first we will pip3 install selenium


#after installing now import selenium
#also just pipinstall all of these
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#right here we need to get a chrome webdriver and then this is how we hop on the webdriver
service = Service(exercutable_path="chromedriver 2")
driver = webdriver.Chrome(service=service)

#driver.get will get us any website we want
driver.get("https://orteil.dashnet.org/cookieclicker/")


#we want to get the inspect element id of the cookie
#so set the cookie id to whatever is on the inspect
cookie_id = "bigCookie"

#we have to wait for the english language xpath to pop up on the site
#we are going to use the xpath for this one this time
webdriverwait = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

#so now once it pops up we want to find the language xpath and then we want to click it
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")

#then we want to click the language
language.click()

#after it clicks on the cookie it needs time to load so we will leave this right so it lets the page load
time.sleep(5)

#now we want to wait for the cookie id to pop up on the site
webdriverwait = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

#now we want to find the cookie id on the site
cookie = driver.find_element(By.ID, cookie_id)

#this is the id for the cookies count
cookies_id = "cookies"

#now this is for the different upgrade we can get include the produce price
product_price_id = "productPrice"
product_prefix = "product"

#now we want to infinite loop the cookie clicking and also print how many cookies we have so we will set up a while loop
while True:
    cookie.click()
    #this is us finding the cookie clicker id and then printing and spliting the text so we only get the cookies text
    #we have the [0] at the end so we only get the number of cookies
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    #we are making it int because it might have commas so we want to get rid of it
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)

#we are doing a for i in range becasue there are only 4 upgrade we can keep upgrading
    
    #the reason we have two different finds is because we are going to find the product price and also the product
    for i in range(4):
        #firs we are going to find the product and also go through the diff number of id's hence the i
        #we add the .replace because we want to replace the text and get rid of the comma with a space 
        product_price = driver.find_element(By.ID, product_price_id + str(i)).text.replace(",", "")

        #we are making sure the product price is a string to fix that is
        if not product_price.isdigit():
            #we will go to the next product
            continue

        #here we will convert the product price to an int so we can compare down below
        product_price = int(product_price)

        #if we have enough cookies we will buy the product
        if cookies_count >= product_price:
            #we are going to find the product and then click on it
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            #once we can buy the product we will break out of the loop because then we will be broke so theres no point in keep tapping the buy
            break

#this jsut be here
time.sleep(10)





