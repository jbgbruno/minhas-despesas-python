from dtos.transaction_dto import TransactionDto
from services.interfaces.transaction_service_interface \
    import TransactionServiceInterface
from repositories.transaction_repository import TransactionRepository
from repositories.interfaces.transaction_repository_interface \
    import TransactionRepositoryInterface


class TransactionService(TransactionServiceInterface):
    def __init__(self):
        self.__repository: TransactionRepositoryInterface = \
            TransactionRepository()

    def create_transaction(self, transaction: TransactionDto):
        self.__repository.create(transaction)
