from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

year = driver.find_element('xpath',"//select[@id='year']")
year_obj = Select(year)

year_obj.select_by_value('2021')
time.sleep(2)
