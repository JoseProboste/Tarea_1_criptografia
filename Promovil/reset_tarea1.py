import selenium
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def selenim():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    for i in range(0,20):
        driver.get("https://www.promovil.cl/contrasena-olvidado")
        driver.find_element_by_name("email").send_keys("astamido911@gmail.com")
        pyautogui.press('enter')
        time.sleep(2)

selenim()