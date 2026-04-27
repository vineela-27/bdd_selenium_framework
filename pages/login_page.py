from selenium.webdriver.common.by import By
from utils.logger import get_logger
import os

logger = get_logger("LoginPage")

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.URL = os.getenv("BASE_URL")

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    message = (By.ID, "flash")

    def open(self):
        logger.info("Opening login page")
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self): 
        self.driver.find_element(*self.login_btn).click()

    def get_message(self):
        return self.driver.find_element(*self.message).text
