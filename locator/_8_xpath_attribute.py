'''

xpath by attribute name and attribute_value
finding the location of web element by using attributes.
-including id, name, class etc ... you can use as a attributes in xpath by attribute
syntax:
<a href:"https://www.amazon.in" id="a1" name="n1" class = "c1" >amazon</a>

syntax:
    //tagname[@attribute_name = 'attribute_value']
    //tagnamep[@name ='attribute_value']

syntax: finding web element by using text
    //tagname[text()="text"]
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.amazon.com/")
driver.maximize_window()
time.sleep(3)

driver.find_element("xpath", "//input[@id='twotabsearchtextbox']").send_keys("Cloth")