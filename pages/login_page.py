from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.customer_page import CustomerPage


class LoginPage(BasePage):
    url_page = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    customer_login_button = (By.XPATH, "//button[text()='Customer Login']")

    def click_to_customer_login(self) -> CustomerPage:
        self._click_to_elm(self.customer_login_button)
        return CustomerPage(self._driver)
