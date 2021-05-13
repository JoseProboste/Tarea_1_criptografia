import selenium
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def selenim():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.promovil.cl/autenticacion?create_account=1")
    driver.find_element_by_name("id_gender").click()
    driver.find_element_by_name("firstname").send_keys("jose")
    driver.find_element_by_name("lastname").send_keys("proboste")
    driver.find_element_by_name("email").send_keys("astamido911@gmail.com")
    driver.find_element_by_name("password").send_keys("123456789")
    driver.find_element_by_name("birthday").send_keys("16/04/1998")
    pyautogui.press('enter')

selenim()