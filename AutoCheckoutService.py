# Note: This code has not been updated. This code was written for educational purposes only, to understand 
# how web scraping works and learn how to use the selenium library.
# The creator of this code does not condone any form of scalping or botting to purchase retail items. 

import pyautogui
import keyboard
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Download the gecko driver from https://github.com/mozilla/geckodriver/releases to be able to launch FireFox.
# Paste the file path into options.executable_path below

options = webdriver.FirefoxOptions()
options.executable_path = "C:\\Users\\YourPathNameHere\\Desktop\\Projects\\geckodriver.exe"

driver = webdriver.Firefox(options=options)


# Copy and paste the URL for whatever item you want to purchase below. 

url = "https://www.smallW.com.au/product/ps5-dualsense-wireless-controller/p/124627/"

driver.get(url)

driver.maximize_window()

# From here, the code you write is going to depend on what website you are using. For example, when the PS5 was in stock at a specific
# retailer, their website would have a green flag on the image of the product, which could be searched for with driver.find_element.abs
# This also allows you to create loops or use WebDriverWait(driver, 10).until(EC.presence_of_element_located(())) to wait until a product
# is in stock. 

# Finds the add to cart button and clicks on it

addtocart = driver.find_element(By.CSS_SELECTOR, 'div.button-group:nth-child(1) > button:nth-child(1)')
addtocart.click()
# Note that the time.sleep is a lazy solution. A better option would be to use Seleniums's WebDriverWait function. 
time.sleep(1)

# Clicks the postcode box. The numbers are the pixels on my screen where this box will appear. Will be different for monitors with different resolutions. 
pyautogui.click(822, 355)

# Types the postcode in
pyautogui.typewrite('1111')

time.sleep(1.3)

# Clicks the suburb. Only use pyautogui if selenium commands dont work. 
pyautogui.click(873, 439)

time.sleep(0.5)

# Press the save button
save = driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/div[3]/button')
save.click()

# Close the pop-up
time.sleep(4)

close = driver.find_element_by_css_selector('.cross > div:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')

close.click()

time.sleep(3)

# Add to cart again
addtocart2 = driver.find_element_by_css_selector('div.ProductAddToCart:nth-child(4) > button:nth-child(1)')

addtocart2.click()

time.sleep(1.2)

# Opening your cart
opencart = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/header/div[3]/div[2]/button[2]')

opencart.click()

time.sleep(1)

# Proceed to checkout
checkout = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/div[2]/div/div[2]/section/div[5]/button')

checkout.click()
time.sleep(1)

# Enter login details
email = driver.find_element_by_id('login__email')
email.send_keys("epicprogram@gmail.com")
password = driver.find_element_by_id('login__password')
password.send_keys("password")

loginbutton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/div/div[1]/form/div[3]/button')
loginbutton.click()
time.sleep(2)

# Proceed to payment
paymentbutton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/section/section/form/div/div/button')
paymentbutton.click()
time.sleep(1.5)

# Enter credit card details
clickcredit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/section/section/section[2]/div[2]/section/div[2]/header/section')
clickcredit.click()
time.sleep(1)
# This is how you scroll down
driver.execute_script("window.scrollTo(0, 633)")
time.sleep(6)
# Credit card number
pyautogui.click(531, 352)
pyautogui.typewrite('12121212121212')
# Month
pyautogui.click(502, 404)
pyautogui.click(406, 505)
# Year
pyautogui.click(800, 410)
pyautogui.click(796, 636)
# CVV
pyautogui.click(654, 490)
pyautogui.typewrite('123')
time.sleep(2)

# Pay now button
pyautogui.click(940, 556)