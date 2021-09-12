import os
from time import sleep

from dotenv import load_dotenv
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()

CARBON_URL = "https://carbon.now.sh?l={language}&code={code}"
CHROMEDRIVER_PATH = os.environ["CHROMEDRIVER_PATH"]


def create_code_image(code: str, language: str, headless: bool = True):
    """Generate a beautiful Carbon code image"""
    options = Options()
    options.headless = headless
    with webdriver.Chrome(CHROMEDRIVER_PATH, options=options) as driver:
        url = CARBON_URL.format(code=code, language=language)
        driver.get(url)
        driver.find_element_by_id("export-menu").click()
        driver.find_element_by_id("export-png").click()
        # make sure it has time to download the image
        sleep(2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create a carbon code image")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", type=str, help="File with code")
    group.add_argument(
        "-c", "--clipboard", action="store_true", help="Use code on clipboard"
    )
    group.add_argument("-s", "--snippet", type=str, help="Code snippet")
    parser.add_argument(
        "-l", "--language", type=str, default="python", help="Code string"
    )
    parser.add_argument(
        "-b", "--browser", action="store_true", default=False,
        help="Run Selenium in interactive (not headless) mode"
    )

    def _get_code(args: argparse.Namespace) -> str:
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

        return code.replace("\n", "%0A")

    args = parser.parse_args()
    code = _get_code(args)
    create_code_image(code, args.language, headless=not args.browser)
