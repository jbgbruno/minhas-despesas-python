from enums.transaction_enum import TransactionType


class TransactionDto:
    def __init__(
        self,
        description,
        value,
        category_id,
        type: TransactionType
    ):
        self.description = description
        self.value = value
        self.category_id = category_id
        self.type = type
