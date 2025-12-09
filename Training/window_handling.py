import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

driver.find_element("xpath","//input[@title='Search for Products, Brands and More']").send_keys('phone')
time.sleep(1)

driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(2)

driver.find_element("xpath","//div[@class='KzDlHZ']").click()
time.sleep(2)

def handle_window():
    return driver.window_handles

for handle in handle_window():
    driver.switch_to.window(handle)
    if 'samsung-galaxy-f36-5g-red-128-gb' in driver.current_url:
        driver.find_element('xpath','//button[text()="Add to cart"]').click()
        time.sleep(2)

driver.find_element('xpath','//a[text()="Help center"]').click()
time.sleep(2)
