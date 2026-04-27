from utils.driver_factory import get_driver
from dotenv import load_dotenv
from datetime import datetime
import os
import base64

def before_all(context):
    load_dotenv()

def before_scenario(context, scenario):
    context.driver = get_driver()

def before_step(context, step):
    print(f"{step.name} {datetime.now()}")
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[@StepTime: {timestamp}]")

def after_step(context, step):
    if step.status == "failed":
        os.makedirs("reports/screenshots", exist_ok=True)

        file_name = f"{step.name.replace(' ', '_')}.png"
        file_path = f"reports/screenshots/{file_name}"

        context.driver.save_screenshot(file_path)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        # Capture screenshot as base64 string
        screenshot_b64 = context.driver.get_screenshot_as_base64()
        
        # Embed the screenshot into the HTML report
        for formatter in context._runner.formatters:
            if "html" in formatter.name:
                formatter.embedding(
                    mime_type="image/png", 
                    data=screenshot_b64, 
                    caption="Failure Screenshot"
                )

    if context.driver:
        context.driver.quit()