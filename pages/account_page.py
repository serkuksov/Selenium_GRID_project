import allure
from selenium.webdriver.common.by import By

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

    @allure.step("Нажатие на кнопку Transactions")
    def click_transactions(self) -> TransactionPage:
        """Нажатие на кнопку Transactions"""
        self._click_to_element(self.transactions_button)
        return TransactionPage(self._driver)

    @allure.step("Нажатие на кнопку Deposit")
    def click_deposit(self) -> None:
        """Нажатие на кнопку Deposit"""
        self._click_to_element(self.deposit_button)

    @allure.step("Нажатие на кнопку Withdrawl")
    def click_withdraw(self) -> None:
        """Нажатие на кнопку Withdrawl"""
        self._click_to_element(self.withdraw_button)

    @allure.step("Пополнить депозит")
    def perform_deposit(self, amount: str):
        """Пополнить депозит"""
        self.click_deposit()
        self._element_visibility(self.deposit_label)
        self.set_input_field_value(amount)
        self.click_submit_form()

    @allure.step("Нажать на кнопку отправки формы")
    def click_submit_form(self):
        """Нажать на кнопку отправки формы"""
        self._click_to_element(self.form_button)

    @allure.step("Ввод значения в поле формы")
    def set_input_field_value(self, amount: str):
        """Ввод значения в поле формы"""
        elm_form = self._find_element(self.form)
        amount_input = self._find_element(self.input, element=elm_form)
        amount_input.clear()
        amount_input.send_keys(amount)

    @allure.step("Вывести средства")
    def perform_withdrawal(self, amount: str):
        """Вывести средства"""
        self.click_withdraw()
        self._element_visibility(self.withdraw_label)
        self.set_input_field_value(amount)
        self.click_submit_form()

    @allure.step("Получить баланс средств")
    def get_balance(self) -> str:
        """Получить баланс средств"""
        balance = self._find_element(self.balance)
        return balance.text
