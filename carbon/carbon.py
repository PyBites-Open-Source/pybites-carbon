import os
from time import sleep
from urllib.parse import quote_plus

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()

CARBON_URL = "https://carbon.now.sh?l={language}&code={code}&bg={background}&t={theme}"
CHROMEDRIVER_PATH = os.environ["CHROMEDRIVER_PATH"]

# in case of a slow connection it might take a bit longer to download the image
SECONDS_SLEEP_BEFORE_DOWNLOAD = int(os.environ.get("SECONDS_SLEEP_BEFORE_DOWNLOAD", 3))

DEFAULT_LANGUAGE = "python"
DEFAULT_BACKGROUND = "#ABB8C3"
DEFAULT_THEME = "seti"


def create_code_image(code: str, **kwargs: str) -> None:
    """Generate a beautiful Carbon code image"""
    language = kwargs.get("language") or DEFAULT_LANGUAGE
    background = kwargs.get("background") or DEFAULT_BACKGROUND
    theme = kwargs.get("theme") or DEFAULT_THEME

    options = Options()
    options.headless = not bool(kwargs.get("interactive", False))
    prefs = {"download.default_directory": kwargs.get("destination", os.getcwd())}
    options.add_experimental_option("prefs", prefs)

    with webdriver.Chrome(CHROMEDRIVER_PATH, options=options) as driver:
        url = CARBON_URL.format(
            language=quote_plus(language),
            code=quote_plus(code),
            background=quote_plus(background),
            theme=quote_plus(theme),
        )
        driver.get(url)
        driver.find_element_by_id("export-menu").click()
        driver.find_element_by_id("export-png").click()
        # make sure it has time to download the image
        sleep(SECONDS_SLEEP_BEFORE_DOWNLOAD)
