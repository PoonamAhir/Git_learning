'''
text = it is a property
'''


from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://myntra.com/")
time.sleep(2)

driver.maximize_window()
time.sleep(1)
'''
data = driver.find_element('xpath','//a[@data-group = "Men"]')
print(data.text)'''

Women = driver.find_element('xpath','//a[text()="Women"][1]')



