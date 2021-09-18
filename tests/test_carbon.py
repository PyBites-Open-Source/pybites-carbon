from pathlib import Path

import pytest

from carbon.carbon import create_code_image

CARBON_DOWNLOAD_FILE = Path("carbon.png")

@pytest.fixture(autouse=True)
def delete_previous_run():
    if CARBON_DOWNLOAD_FILE.exists():
        CARBON_DOWNLOAD_FILE.unlink()


def test_create_standard_python_code_image():
    create_code_image("print('hello world')")
    assert CARBON_DOWNLOAD_FILE.exists()
