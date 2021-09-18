from pathlib import Path

import pytesseract

from carbon.carbon import create_code_image

CARBON_DOWNLOAD_FILE = Path("carbon.png")
LONGER_CODE_SNIPPET = """
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:8000/")
        yield driver
    except WebDriverException:
        raise RuntimeError("Cannot get to localhost:8000, did you start FastAPI?")
    finally:
        driver.quit()
"""


def test_create_image_for_one_liner():
    create_code_image("print('hello world')")
    assert CARBON_DOWNLOAD_FILE.exists()
    image_text = pytesseract.image_to_string(CARBON_DOWNLOAD_FILE.name)
    assert "hello world" in image_text


def test_create_image_for_larger_snippet():
    create_code_image(LONGER_CODE_SNIPPET)
    assert CARBON_DOWNLOAD_FILE.exists()
    image_text = pytesseract.image_to_string(CARBON_DOWNLOAD_FILE.name)
    # not getting full text, but at least some snippets which show it worked
    assert "fixture" in image_text
    assert "Chrome" in image_text
    assert "yield" in image_text
    assert "except" in image_text
