import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.find_element('name', 'firstname').send_keys('Poonam')
time.sleep(1)
driver.find_element('name', 'lastname').send_keys('Ahir')
time.sleep(1)

driver.find_element('name', 'reg_email__').send_keys('Poonam12@gmail.com')
time.sleep(1)
driver.find_element('name', 'reg_passwd__').send_keys('Poonam@123')
time.sleep(1)