from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base import Base


class DBConnectionHandler:

    def __init__(self) -> None:
        # self.__connection_string = 'mysql+pymysql://root:root@\
        #     localhost:3306/meu_dinheiro'
        self.__connection_string = 'mysql+pymysql://root:root@localhost:3306\
            /meu_dinheiro'

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        Base.metadata.create_all(engine)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
