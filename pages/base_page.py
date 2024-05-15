from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    url_page: str

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self._driver = driver
        self.timeout = timeout
        if self.__check_url(self.url_page) is False:
            raise ValueError(
                f"Страница {self._get_url()} не соответствует классу: {self.__class__.__name__}"
            )

    def __check_url(self, url_page: str, timeout=None) -> bool:
        """Проверка наличия в URL текущей страницы текста url_page"""
        if timeout is None:
            timeout = self.timeout
        try:
            WebDriverWait(self._driver, timeout).until(EC.url_contains(url_page))
            return True
        except TimeoutException:
            return False

    def _get_title(self) -> str:
        """Получить Title страницы"""
        return self._driver.title

    def _get_url(self) -> str:
        """Получить URL страницы"""
        return self._driver.current_url

    def _find_element(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> WebElement:
        """Получить элемент страницы"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._driver
        return WebDriverWait(element, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def _find_elements(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> list[WebElement]:
        """Получить список элементов страницы"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._driver
        return WebDriverWait(element, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def _get_clickable_element(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> WebElement:
        """Получить кликабельный элемент"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._driver
        return WebDriverWait(element, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def _click_to_elm(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> None:
        """Кликнуть по элементу"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._driver
        elm = self._get_clickable_element(locator, element=element, timeout=timeout)
        elm.click()

    def _element_visibility(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> bool:
        """Проверить видимость элемента на странице"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._driver
        try:
            WebDriverWait(element, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True
