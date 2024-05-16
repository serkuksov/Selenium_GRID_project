import csv
import os
from datetime import datetime

from config import PATH_TO_DIR_CSV_REPORTS
from utils.shems import Transaction


class TransactionsCSVReport:
    """Класс для формирования отчетов по транзакциям"""

    def __init__(
        self, transactions: list[Transaction], name_csv_report: str | None = None
    ) -> None:
        self.transactions = transactions
        self._name_csv_report = None
        if name_csv_report is not None:
            self._name_csv_report = name_csv_report

    def generate_csv_report(self) -> None:
        """Генерация отчета"""
        path_to_file = os.path.join(PATH_TO_DIR_CSV_REPORTS, self.name_csv_report)
        name_columns = [
            "Дата-времяТранзакции",
            "Сумма",
            "ТипТранзакции",
        ]
        with open(path_to_file, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(name_columns)
            for transaction in self.transactions:
                list_params_transaction = [
                    transaction.datetime_transacted.strftime("%d %B %Y %H:%M:%S"),
                    transaction.amount,
                    transaction.transaction_type.value,
                ]
                writer.writerow(list_params_transaction)

    @property
    def name_csv_report(self) -> str:
        """Название файла отчета"""
        if self._name_csv_report is None:
            datetime_str = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            self._name_csv_report = f"transactions_{datetime_str}.csv"
        return self._name_csv_report
