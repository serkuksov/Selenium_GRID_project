from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class TransactionType(Enum):
    """Типы транзакций"""

    CREDIT = "Credit"
    DEBIT = "Debit"


class Transaction(BaseModel):
    """Схема транзакции"""

    datetime_transacted: datetime
    amount: int
    transaction_type: TransactionType
