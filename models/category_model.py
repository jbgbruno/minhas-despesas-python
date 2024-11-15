from database.base import Base
from sqlalchemy import Column, Integer, String


class CategoryModel(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))

    def __repr__(self):
        return f"Category(id={self.id}, nome={self.name},\
        descricao={self.description})"
