'''
Class Name:
- It is used to find the web element in a webpage by using attribute called 'class'
- if any space is there in the locator value you should replace with dot(.)
- class and class name both are different
- class is an attribute which is present in the html and class name is a locator which is present in selenium
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/register")

driver.maximize_window()
time.sleep(3)

driver.find_element("class name", "text-box.single-line").send_keys("Poonam")
time.sleep(1)