import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def selenim():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.arrow.cl/registro?back=my-account")
    driver.find_element_by_name("email").send_keys("sonicgocu@hotmail.com")
    driver.find_element_by_name("passwd").send_keys("123456789")
    driver.find_element_by_id("SubmitLogin").click()
    
selenim()