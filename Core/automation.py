from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random, time, Core.configure as config

class Automation:

    def sign_in(driver):

        # make a request
        driver.get(config.LOGIN_URL)

        # waiting method
        wait = WebDriverWait(driver, 10)

        # find this field and write the text like a human
        email_input = wait.until(EC.presence_of_element_located((By.NAME, 'session_key')))
        pass_input  = wait.until(EC.presence_of_element_located((By.NAME, 'session_password')))
        sign_in_button  = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign in')]")))

        # make selenuim write
        Automation.writing_input(email_input, config.EMAIL)
        time.sleep(random.uniform(0.4, 2))

        Automation.writing_input(pass_input, config.PASSWORD)
        time.sleep(random.uniform(0.4, 2))

        sign_in_button.click()

        return driver
    

    def writing_input(element, text):
        element.clear()

        for char in text:

            if random.uniform(0,1):
                element.send_keys(char)
                time.sleep(random.uniform(0.05, 0.02))
            else:
                element.send_keys(char)
                time.sleep(random.uniform(0.2, 0.04))

            
        