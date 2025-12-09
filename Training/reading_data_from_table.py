from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(2)


for i in range(2, 8):
    for j in range(1, 5):
        data = driver.find_element('xpath',f"//table[@name='BookTable']//tr[{i}]/td[{j}]")
        print(data.text,end='\t')
    print()
