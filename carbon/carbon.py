import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

CARBON_URL = (
    "https://carbon.now.sh?l={language}&code={code}"
    "&bg={background}&t={theme}&wt={wt}"
)


def _create_carbon_url(code, **carbon_options: str) -> str:
    language = carbon_options["language"]
    background = carbon_options["background"]
    theme = carbon_options["theme"]
    wt = carbon_options["wt"]

    url = CARBON_URL.format(
        language=quote_plus(language),
        code=quote_plus(code),
        background=quote_plus(background),
        theme=quote_plus(theme),
        wt=quote_plus(wt),
    )
    return url


def create_code_image(code: str, **kwargs: str) -> None:
    """Generate a beautiful Carbon code image"""
    destination = kwargs.get("destination", os.getcwd())
    headless = kwargs.get("headless", True)

    with sync_playwright() as p:
        with p.chromium.launch(headless=headless) as browser:
            context = browser.new_context()
            page = context.new_page()
            url = _create_carbon_url(code, **kwargs)
            page.goto(url)

            page.click("#export-menu")
            page.click("#export-png")

            download = page.wait_for_event("download")
            download_path = os.path.join(destination, "carbon_image.png")
            download.save_as(download_path)
