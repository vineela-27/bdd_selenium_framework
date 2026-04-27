from selenium import webdriver
import os

def get_driver():
    browser = os.getenv("BROWSER", "chrome").lower()
    is_ci = os.getenv("CI") or os.getenv("GITHUB_ACTIONS")
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        
        # CI/CD environment flags (GitHub Actions, Docker, etc.)
        if is_ci:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-default-apps")
            options.add_argument("--disable-sync")
            options.add_argument("--disable-notifications")
        
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        
        if is_ci:
            options.add_argument("--headless")
        
        return webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        
        if is_ci:
            options.add_argument("--headless")
        
        return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
