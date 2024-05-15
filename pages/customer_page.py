from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.account_page import AccountPage
from pages.base_page import BasePage


class CustomerPage(BasePage):
    url_page = (
        "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
    )
    elm_select_customer = (By.XPATH, "//select[@id='userSelect']")
    customer_login_button = (By.XPATH, "//button[text()='Login']")

    def select_customer(self, customer_name: str) -> None:
        """Выбор клиента по имени"""
        select = Select(self._find_element(self.elm_select_customer))
        select.select_by_visible_text(customer_name)

    def click_login(self) -> AccountPage:
        """Вход в систему"""
        self._click_to_elm(self.customer_login_button)
        return AccountPage(self._driver)
