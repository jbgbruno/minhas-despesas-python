from models.transaction_model import TransactionModel
from repositories.interfaces.transaction_repository_interface \
    import TransactionRepositoryInterface
from dtos.transaction_dto import TransactionDto
from database.connection import DBConnectionHandler
from sqlalchemy.orm.exc import NoResultFound


class TransactionRepository(TransactionRepositoryInterface):

    def get(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(TransactionModel).all()
                return data

            except Exception as exception:
                db.session.rollback()
                raise exception

    def get_by_id(self, id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(TransactionModel)\
                    .filter_by(id=id)\
                    .first()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def create(self, transaction: TransactionDto):
        with DBConnectionHandler() as db:
            try:
                model = TransactionModel(
                    description=transaction.description,
                    value=transaction.value,
                    category_id=int(transaction.category_id),
                    type=transaction.type.value
                )
                db.session.add(model)
                db.session.commit()
                return True
            except Exception as exception:
                db.session.rollback()
                raise exception
