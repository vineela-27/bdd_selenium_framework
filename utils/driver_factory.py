from selenium import webdriver
import os

def get_driver():
    browser = os.getenv("BROWSER", "chrome").lower()
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        return webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
