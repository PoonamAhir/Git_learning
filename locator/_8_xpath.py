'''
firth seventh locators doesn't support indexing(drawback of first 7th locator)
locating text is also difficult.
--------------
any problem you have to finding web elements it can solve it using xpath
--------------------------------------------------
xpath:
xpath is used to find the location of web element in a html tree structure or in DOM(Document Object Model)

xpath is classified in two_types:
1. Absolute path : starts from the root of html tree.
2. Relative path.

1.Absolute xpath
     -->It will traverse from parent to its own child
     -->It is Denoted as (/)
    ->Drawbacks of Absolute xpath
     -->Absolute xpath is very lengthy comparing to relative xpath
     --> Always it will traverse from parent to its own child
2.Relative xpath
     -->It will traverse from parent to any of the child
     -->It is Denoted as (//)
     --> doesn't start with root of html tree.

Sample for Absolute xpath
----------------------------------
driver = http://webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[1]/input[1]").send_keys("Username1")


driver = http://webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[2]/input[2]").send_keys("Username4")


driver = http://webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)
driver.find_element("xpath","html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
'''

#relative
#driver.find_element("xpath", "//div[1]/div[1]/input[1]").send_keys("Poonam")
time.sleep(2)

