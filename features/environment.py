from utils.driver_factory import get_driver
from dotenv import load_dotenv

def before_all(context):
    load_dotenv()

def before_scenario(context, scenario):
    context.driver = get_driver()

def after_scenario(context, scenario):
    context.driver.quit()
