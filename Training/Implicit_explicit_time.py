from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
wait_ = WebDriverWait(driver, 10)
'''
driver.implicitly_wait(15)

driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(1)
driver.find_element('xpath',"(//input[@name='btnI')[2]]").click()
time.sleep(2)
'''
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element('id', 'user-name').send_keys('standard_user')
time.sleep(1)
driver.find_element('id','password').send_keys('secret')
time.sleep(1)
driver.find_element('id','login-button').click()
time.sleep(2)

if wait_.until(expected_conditions.url_contains("inventory")):
    print('successfully logged in')
else:
    print('failed to log in')