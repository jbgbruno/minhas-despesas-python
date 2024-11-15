from database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class TransactionModel(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    description = Column(String(255))
    value = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    type = Column(Integer)

    def __repr__(self):
        return f"Transaction(id={self.id}, description={self.description},\
        value={self.value}, category_id={self.category_id},\
        type={self.type})"
