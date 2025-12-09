'''
sample html:
- <a href="https://www.google.com">Google</a>

A html code consists of three components
1. Tagname
2. Attribute
3. text
'''

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Poonam/OneDrive/Desktop/Qspiders/Poonam.html")

time.sleep(3)
driver.maximize_window()
time.sleep(2)

driver.find_element("tag name","a").click()
time.sleep(1)