import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def selenim():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.arrow.cl/registro?back=my-account#account-creation")
    driver.find_element_by_id("email_create").send_keys("astamido911@gmail.com")
    driver.find_element_by_name("SubmitCreate").click()
    driver.find_element_by_id("customer_firstname").send_keys("jose")
    driver.find_element_by_id("customer_lastname").send_keys("proboste")
    driver.find_element_by_id("days").send_keys("16")
    driver.find_element_by_id("birthday").send_keys("4")
    driver.find_element_by_id("years").send_keys("1998")
    driver.find_element_by_id("id_gender1").click()
    driver.find_element_by_id("passwd").send_keys("123456789")

selenim()