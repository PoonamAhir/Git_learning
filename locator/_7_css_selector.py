'''
Css stands for Cascading style sheet
it is used to decorate the webpage like color, fond, size,
background ect ....

what is css selector:
it is used to find the web element by using css expression
syntax:
    tagname[attribute name = 'attribute value']
any attribute including id, name, class, etcc....

step1: inspect the element
step2: press ctrl + f your keyboard "find my string" search will get appear
step3: type the css expression

"verify the css expression to check if the expression is valid or not
1. Element should get highlight
2. code should highlight is yellow color
3. (1 on 1) matching you have to get
'''

'''
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
time.sleep(2)

driver.find_element("css selector", "input[class='email']").send_keys("PoonamAhir@gmail.com")
time.sleep(2)
driver.find_element("css selector","input[class='password']").send_keys("password")
time.sleep(2)
driver.find_element("id", "RememberMe").click()
time.sleep(2)
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.facebook.com/")
time.sleep(1)
driver.maximize_window()
time.sleep(1)
driver.find_element("css selector","a[class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
time.sleep(1)

driver.find_element("name","firstname").send_keys("Poonam")
driver.find_element("name", "lastname").send_keys("Ahir")
time.sleep(1)

driver.find_element("id","sex").click()
time.sleep(1)
driver.find_element("name","reg_email__").send_keys("Poonam.ahir@gmail.com")
time.sleep(1)
driver.find_element("id","password_step_input").send_keys("password")
time.sleep(1)

driver.find_element("name","websubmit").click()
time.sleep(1)
