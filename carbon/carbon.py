import os
from time import sleep
from urllib.parse import quote_plus

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()

CARBON_URL = "https://carbon.now.sh?l={language}&code={code}"
CHROMEDRIVER_PATH = os.environ["CHROMEDRIVER_PATH"]
# in case of a slow connection it might take a bit longer to download the image
SECONDS_SLEEP_BEFORE_DOWNLOAD = int(os.environ.get("SECONDS_SLEEP_BEFORE_DOWNLOAD", 3))


def create_code_image(code: str, language: str, headless: bool = True):
    """Generate a beautiful Carbon code image"""
    options = Options()
    options.headless = headless
    with webdriver.Chrome(CHROMEDRIVER_PATH, options=options) as driver:
        encoded_code = quote_plus(code)
        url = CARBON_URL.format(code=encoded_code, language=language)
        driver.get(url)
        driver.find_element_by_id("export-menu").click()
        driver.find_element_by_id("export-png").click()
        # make sure it has time to download the image
        sleep(SECONDS_SLEEP_BEFORE_DOWNLOAD)
