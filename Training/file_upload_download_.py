from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

#driver = webdriver.Chrome(opts)
'''
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(3)
driver.maximize_window()
time.sleep(1)

file1 = r"C:\Users\Poonam\OneDrive\Desktop\Selenium\sample.html"
file2 = r"C:\Users\Poonam\OneDrive\Desktop\Selenium\Poonam.html"

driver.find_element("xpath","//input[@id='multipleFilesInput']").send_keys(f'{file1}\n{file2}')
time.sleep(2)
'''

prefs = {
    'download.default_directory' : r'C:\Users\Poonam\Desktop\Selenium',
    'download.prompt_for_download' : False,
    'safebrowsing.enabled' : True,
    'plugins.always_open_pdf_externally' : True
}

opts.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/upload-download')
time.sleep(2)
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath','//a[text()="Download"]').click()
