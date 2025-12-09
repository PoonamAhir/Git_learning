#17-11-2025
from selenium import webdriver
import time

from selenium.webdriver import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

'''
driver.get("https://demowebshop.tricentis.com")
time.sleep(3)
driver.maximize_window()
time.sleep(1)


1)
footer_elements = driver.find_elements("xpath","//div[@class='footer-menu-wrapper']//h3")
#web_elements: [Wb1, Wb2, Wb3, Wb4, Wb5, Wb6, Wb7, Wb8.........Wbxy](list of web elements)
for element in footer_elements:
    print(element.text)'''

'''2)
content = driver.find_elements("xpath","//div[@class='block block-category-navigation']//a")

for con in content:
    print(con.text)'''

#3)WAP fetch the popular search in myntra


driver.get("https://www.myntra.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(1)

driver.find_element("xpath","//input[@class='desktop-searchBar']").send_keys("adidas")
time.sleep(2)
driver.find_element("xpath","//li[text()='Adidas Shoes']").click()
time.sleep(2)

product_name = driver.find_elements("xpath","//h4[@class='product-product']")
product_price = driver.find_elements("xpath","//div[@class='product-price']")

for name, price in zip(product_name, product_price):
    print(name.text,'==', price.text)
