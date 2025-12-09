'''
dependent and independent element xpath:
- Indentify the dependent element
- write the xpath of the independent element
- Traverse back until we get the common match for dependent independent element
- when user click and both independent and dependent web element highlight then we can call it as "back traversing"
- continue writing the xpath of the dependent element

syntax:
//tagname[text()="text"]/..

"text" ->dependent element text(name)

single step back traversing until we get the common match for dependent independent element ->
/.. -> just go to immediate parent.

//[independent_element xpath]/..//[dependent_element_xpath]
e.g:
//tagname[text()="text"]/..//tagname[@name="value"]
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://in.tradingview.com/")
time.sleep(3)

driver.maximize_window()
time.sleep(2)

driver.find_element("xpath", "//span[text()='Search']").click()
time.sleep(1)

driver.find_element("xpath", "//input[@name='query']").send_keys("HAL")
time.sleep(2)

driver.find_element("xpath","(//button[@aria-label='Search'])[3]").click()
time.sleep(2)

driver.find_element("xpath", "//button[text()='Search']").click()
time.sleep(2)

containt = driver.find_element("xpath","//span[text()='HAL']/..//span[@class='priceWrapper-qWcO4bp9']")