'''
Contains : to locate the partial text of any tagname, we use xpath using contains

//tagname[contains(text(),"text"]
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.giva.co/")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

#//span[contains(text(), "gold with lab Diamonds")')].click()
#

