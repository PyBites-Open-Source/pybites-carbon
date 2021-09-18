from pathlib import Path

import pytest
import pytesseract

from carbon.carbon import _create_carbon_url, create_code_image

CARBON_DOWNLOAD_FILE = Path("carbon.png")
ONE_LINE_SNIPPET = """print('hello world')"""
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
    create_code_image(ONE_LINE_SNIPPET)
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


def test_storing_image_in_different_folder(tmpdir):
    carbon_file = tmpdir / CARBON_DOWNLOAD_FILE
    if carbon_file.exists():
        carbon_file.unlink()
    assert not carbon_file.exists()
    create_code_image(ONE_LINE_SNIPPET, destination=tmpdir.strpath)
    assert carbon_file.exists()


@pytest.mark.parametrize(
    "code, kwargs, expected",
    [
        ("hello", {}, "https://carbon.now.sh?l=python&code=hello&bg=%23ABB8C3&t=seti"),
        (
            "hello",
            {"language": "javascript"},
            "https://carbon.now.sh?l=javascript&code=hello&bg=%23ABB8C3&t=seti",
        ),
        (
            "hello world",
            {},
            "https://carbon.now.sh?l=python&code=hello+world&bg=%23ABB8C3&t=seti",
        ),
        (
            "print('hello world')",
            {},
            "https://carbon.now.sh?l=python&code=print%28%27hello+world%27%29&bg=%23ABB8C3&t=seti",
        ),
        (
            "hello",
            {"theme": "material"},
            "https://carbon.now.sh?l=python&code=hello&bg=%23ABB8C3&t=material",
        ),
        (
            "hello",
            {"background": "#C4F2FD"},
            "https://carbon.now.sh?l=python&code=hello&bg=%23C4F2FD&t=seti",
        ),
        (
            "hello",
            {"background": "#D7FFC5", "theme": "text"},
            "https://carbon.now.sh?l=python&code=hello&bg=%23D7FFC5&t=text",
        ),
    ],
)
def test_create_carbon_url(code, kwargs, expected):
    assert _create_carbon_url(code, **kwargs) == expected
