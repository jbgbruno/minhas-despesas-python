from abc import ABC, abstractmethod
from dtos.transaction_dto import TransactionDto


class TransactionRepositoryInterface(ABC):

    @abstractmethod
    def get(self): ...

    @abstractmethod
    def get_by_id(self, id): ...

    @abstractmethod
    def create(self, transaction: TransactionDto): ...
