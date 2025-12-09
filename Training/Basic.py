from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.chrome(opts)

driver.get("https://www.google.com")
