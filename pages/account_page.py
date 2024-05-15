from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.transaction_page import TransactionPage


class AccountPage(BasePage):
    url_page = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
    form = (By.XPATH, "//form[@name='myForm']")
    input = (By.XPATH, "//input[@ng-model='amount']")
    form_button = (By.XPATH, f"{form[1]}/button")
    withdraw_label = (By.XPATH, "//label[contains(text(), 'Withdraw')]")
    deposit_label = (By.XPATH, "//label[contains(text(), 'Deposit')]")
    transactions_button = (By.XPATH, "//button[contains(text(), 'Transactions')]")
    deposit_button = (By.XPATH, "//button[contains(text(), 'Deposit')]")
    withdraw_button = (By.XPATH, "//button[contains(text(), 'Withdraw')]")
    balance = (By.XPATH, "//div[@ng-hide='noAccount']/strong[2]")

    def click_transactions(self) -> TransactionPage:
        """Нажатие на кнопку Transactions"""
        self._click_to_elm(self.transactions_button)
        return TransactionPage(self._driver)

    def click_deposit(self, element: WebElement = None) -> None:
        """Нажатие на кнопку Deposit"""
        self._click_to_elm(self.deposit_button, element=element)

    def click_withdraw(self, element: WebElement = None) -> None:
        """Нажатие на кнопку Withdrawl"""
        self._click_to_elm(self.withdraw_button, element=element)

    def perform_deposit(self, amount: str):
        """Пополнить депозит"""
        self.click_deposit()
        self._element_visibility(self.deposit_label)
        elm_form = self._find_element(self.form)
        amount_input = self._find_element(self.input, element=elm_form)
        amount_input.clear()
        amount_input.send_keys(amount)
        self._click_to_elm(self.form_button)

    def perform_withdrawal(self, amount: str):
        """Вывести средства"""
        self.click_withdraw()
        self._element_visibility(self.withdraw_label)
        elm_form = self._find_element(self.form)
        amount_input = self._find_element(self.input, element=elm_form)
        amount_input.clear()
        amount_input.send_keys(amount)
        self._click_to_elm(self.form_button)

    def get_balance(self) -> str:
        balance = self._find_element(self.balance)
        return balance.text
