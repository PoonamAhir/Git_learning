from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",  True)
driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)


'''
driver.get("https://www.myntra.com")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

women = driver.find_element('xpath', "(//a[text()='Women'])[1]")
ac_obj.move_to_element(women).perform()
time.sleep(2)
'''
##################################################################
'''Double click


driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

copy_ele = driver.find_element('xpath', "(//button[text()='Copy Text'])")
ac_obj.double_click(copy_ele).perform()
time.sleep(2)'''

##################################################################
'''context_click

ele = driver.find_element('xpath', "//h2[text()='Dynamic Button']")
ac_obj.context_click(ele).perform()
time.sleep(2)'''

#ac_obj.context_click().perform() -->it will right click at the start of application.

##################################################################
'''Scrolling

driver.get("https://www.myntra.com")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

#ele = driver.find_element('xpath', "")
#ac_obj.send_keys(Keys.END).perform()
#time.sleep(2)
#ac_obj.send_keys(Keys.HOME).perform()

ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_UP).perform()
time.sleep(2)
'''

#############################################################
'''scroll Down and scroll up by pixels

driver.get("https://www.myntra.com")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

driver.execute_script("window.scrollBy(0, 500);") #will scroll down 500 pixels
time.sleep(2)
driver.execute_script("window.scrollBy(0, 500);") #will scroll up 500 pixels
time.sleep(2)
'''
###########################################################
'''drag and drop button

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

ele = driver.find_element('xpath', "//h2[text()='Slider']")
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

draggable_ele = driver.find_element('xpath', "//div[@id='draggable']")
droppable_ele = driver.find_element('xpath', "//div[@id='droppable']")

ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()
time.sleep(2)
'''
#############################################################################################
'''slider'''

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

ele = driver.find_element('xpath', "//h2[text()='SVG Elements']")
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

slider = driver.find_element('xpath', "//div[@id='slider']")