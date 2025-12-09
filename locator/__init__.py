'''



'''


from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.google.com")
time.sleep(3)
driver.maximize_window(2)
time.sleep(2)