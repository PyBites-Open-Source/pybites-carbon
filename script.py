import argparse
import os
from time import sleep
from urllib.parse import quote_plus

from dotenv import load_dotenv
import pyperclip
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


def get_args():
    parser = argparse.ArgumentParser(description="Create a carbon code image")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", type=str, help="File with code")
    group.add_argument(
        "-c", "--clipboard", action="store_true", help="Use code on clipboard"
    )
    group.add_argument("-s", "--snippet", type=str, help="Code snippet")
    parser.add_argument(
        "-l", "--language", type=str, default="python", help="Programming language"
    )
    parser.add_argument(
        "-b",
        "--browser",
        action="store_true",
        default=False,
        help="Run Selenium in interactive (not headless) mode",
    )
    return parser.parse_args()


def get_code(args: argparse.Namespace) -> str:
    """
    Argparse's add_mutually_exclusive_group already guaranteers
    we get one of clipboard, file or snippet
    """
    if args.clipboard:
        code = pyperclip.paste()
    elif args.file:
        with open(args.file) as f:
            code = f.read()
    else:
        code = args.snippet

    return code


def main():
    args = get_args()
    code = get_code(args)
    create_code_image(code, args.language, headless=not args.browser)


if __name__ == "__main__":
    main()
