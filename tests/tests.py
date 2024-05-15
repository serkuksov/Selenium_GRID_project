from time import sleep

from pages.login_page import LoginPage
from utils.calculate_fibonacci import calculate_fibonacci_for_today
from utils.csv_report import TransactionsCSVReport


def test_banking_operations(driver):
    # Шаг 1: Открытие начальной страницы
    driver.get(LoginPage.url_page)
    assert "XYZ Bank" in driver.title

    # Шаг 2: Открытие страницы авторизации пользователя
    login_page = LoginPage(driver)
    customer_page = login_page.click_to_customer_login()

    # Шаг 3: Авторизация пользователя
    customer_page.select_customer(customer_name="Harry Potter")
    account_page = customer_page.click_login()

    # Шаг 3: Пополнение счета
    balance = account_page.get_balance()
    assert balance == "0"

    fib_number = str(calculate_fibonacci_for_today())

    account_page.perform_deposit(fib_number)
    balance = account_page.get_balance()
    assert fib_number == balance

    # Шаг 4: Списание со счета
    account_page.perform_withdrawal(fib_number)
    balance = account_page.get_balance()
    assert balance == "0"

    sleep(2)
    transaction_page = account_page.click_transactions()
    transactions = transaction_page.get_list_transaction()
    assert len(transactions) == 2
    assert transactions[0].amount == int(fib_number)

    # Шаг 5: Формирование CSV отчета
    report = TransactionsCSVReport(transactions)
    report.generate_csv_report()

    name_csv_report = report.name_csv_report
