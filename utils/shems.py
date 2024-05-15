from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class TypeTransacted(Enum):
    """Типы транзакций"""

    CREDIT = "Credit"
    DEBIT = "Debit"


class Transaction(BaseModel):
    """Схема транзакции"""

    datetime_transacted: datetime
    amount: int
    type_transacted: TypeTransacted
