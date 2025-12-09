'''
tagname = [text()="text"]

Occurrences:
1. Similar number of web elements on same page
in that case we can use group indexing:

grouping => //tagname[text()="text"]
(grouping)[web_element_index_number]

'''
from selenium import webdriver
import time

from selenium.webdriver import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

'''
driver.get("http://flipkart.com")
time.sleep(3)
driver.maximize_window()
time.sleep(1)
driver.find_element("xpath","//span[text()='TVs & Appliances']").click()
time.sleep(2)

driver.get("https://www.amazon.in")
time.sleep(3)
driver.maximize_window()
time.sleep(2)

driver.find_element("xpath","//a[text()='Gift Cards']").click()  #need to change
time.sleep(1)

driver.get("https://blinkit.com/")
time.sleep(2)

driver.maximize_window()
time.sleep(1)

driver.find_element("xpath","//button[text()='Detect my location']").click()
time.sleep(2)

driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(3)

driver.maximize_window()
time.sleep(1)

driver.find_element("xpath","(//input[@type='text'])[1]").send_keys("Poonam")
time.sleep(1)

driver.find_element("xpath","(//input[@type='text'])[2]").send_keys("Ahir")
time.sleep(1)

driver.find_element("xpath","(//input[@type='text'])[5]").send_keys("punamahir09@gmail.com")
time.sleep(1)

driver.find_element("xpath","//input[@type='password']").send_keys("Poonam")
time.sleep(2)
'''



