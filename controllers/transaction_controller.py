from dtos.transaction_dto import TransactionDto
from services.interfaces.transaction_service_interface \
    import TransactionServiceInterface
from services.transaction_service import TransactionService


class TransactionController:
    def __init__(self):
        self.__service: TransactionServiceInterface = TransactionService()

    def create_transaction(self, transaction: TransactionDto) -> bool:
        return self.__service.create_transaction(transaction)
