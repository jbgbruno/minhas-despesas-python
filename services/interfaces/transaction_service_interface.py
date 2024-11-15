from abc import ABC, abstractmethod
from dtos.transaction_dto import TransactionDto


class TransactionServiceInterface(ABC):
    @abstractmethod
    def create_transaction(self, transaction: TransactionDto): ...
