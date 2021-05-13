import selenium
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def selenim():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.arrow.cl/recuperar-contrasena")
    driver.find_element_by_name("email").send_keys("sonicgocu@hotmail.com")
    pyautogui.press('enter')

selenim()