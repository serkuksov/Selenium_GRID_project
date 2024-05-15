from datetime import datetime
from time import sleep

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from utils.shems import Transaction
from pages.base_page import BasePage


class TransactionPage(BasePage):
    url_page = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx"
    table_rows = (By.XPATH, "//table/tbody/tr")
    table_cells = (By.TAG_NAME, "td")

    def get_list_transaction(self) -> list[Transaction]:
        """Нажатие на кнопку Transactions"""
        elm_table_rows = self._find_elements(self.table_rows)
        transactions = []
        for elm_table_row in elm_table_rows:
            cells = elm_table_row.find_elements(*self.table_cells)
            datetime_transacted = self.get_formatted_datetime(cells[0].text)
            amount = int(cells[1].text)
            type_transacted = cells[2].text
            transaction = Transaction(
                datetime_transacted=datetime_transacted,
                amount=amount,
                type_transacted=type_transacted,
            )
            transactions.append(transaction)
        return transactions

    @staticmethod
    def get_formatted_datetime(datetime_str: str) -> datetime:
        """Получение объекта datetime из строки вида: May 14, 2024 11:34:39 PM"""
        return datetime.strptime(datetime_str, "%b %d, %Y %I:%M:%S %p")
