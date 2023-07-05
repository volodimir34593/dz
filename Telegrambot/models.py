from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, ForeignKey

from db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    name = Column(
        Unicode(255),
        nullable=False,
    )
    size = Column(
        Unicode(255),
        nullable=False,
    )
    price = Column(
        Unicode(255),
        nullable=False,
    )
    color = Column(
        Unicode(255),
        nullable=False,
    )
    #ref_countries_id

    def __repr__(self)->str:
        return f'''Name:{self.name}\nSize: {self.size}\nPrice: {self.price}\nColor: {self.color}'''