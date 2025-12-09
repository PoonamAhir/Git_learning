import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.find_element('id','name').send_keys('Poonam')
time.sleep(1)
driver.find_element('id','email').send_keys('poonam@gmail.com')
time.sleep(1)
driver.find_element('id','phone').send_keys('9860340898')
time.sleep(1)
driver.find_element('id', 'textarea').send_keys('Bengaluru')
time.sleep(1)
driver.find_element('id', 'female').click()
time.sleep(1)
driver.find_element('id', 'wednesday').click()
time.sleep(1)

driver.find_element('id', 'country').click()
time.sleep(1)


