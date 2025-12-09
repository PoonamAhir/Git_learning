from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/register")
time.sleep(3)
driver.maximize_window()
time.sleep(2)

driver.find_element("id","gender-female").click()
time.sleep(2)
driver.find_element("id","FirstName").send_keys("Kshitij")
time.sleep(2)
driver.find_element("id","LastName").send_keys("patil")
time.sleep(2)
driver.find_element("id","Email").send_keys("Kshitijpatil@gmail.com")
time.sleep(2)
driver.find_element("id","Password").send_keys("Kshitij@123")
time.sleep(2)
driver.find_element("id","ConfirmPassword").send_keys("Kshitij@123")
time.sleep(2)
driver.find_element("id","register-button").click()
time.sleep(2)
