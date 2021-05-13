import selenium
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def selenim():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.promovil.cl/autenticacion?back=my-account")
    driver.find_element_by_name("email").send_keys("sonicgocu@hotmail.com")
    driver.find_element_by_name("password").send_keys("rikito123")
    driver.find_element_by_id("submit-login").click()
    driver.get("https://www.promovil.cl/identidad")
    driver.find_element_by_name("password").send_keys("rikito123")
    driver.find_element_by_name("new_password").send_keys("123456789")
    pyautogui.press('enter')
    
selenim()