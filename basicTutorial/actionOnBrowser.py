from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    baseUrl = "https://www.facebook.com/login/"
    driver = webdriver.Chrome()
    driver.get(baseUrl)
    driver.maximize_window();

    driver.implicitly_wait(10);

    emailField = driver.find_element_by_xpath("//input[@name='email']")
    emailField.send_keys('nishikant.singh.585')

    passwordField = driver.find_element_by_xpath("//input[@name='pass']")
    passwordField.send_keys('bratvabhoodhello')

    time.sleep(5)

    logInLink = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
    logInLink.click()
    print(driver.current_url)

