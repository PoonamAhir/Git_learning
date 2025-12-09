from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.selenium.dev/downloads/")
time.sleep(3)
driver.maximize_window()
time.sleep(2)
driver.find_element("partial link text", "languages").click()
time.sleep(2)