from typing import Generator

import pytest
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from config import SELENIUM_SERVER_URL


@pytest.fixture(scope="module")
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура для получения драйвера selenium"""

    options = Options()
    options.set_capability("browserName", "chrome")

    driver = Remote(command_executor=SELENIUM_SERVER_URL, options=options)
    try:
        yield driver
    finally:
        driver.quit()
