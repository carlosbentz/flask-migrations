from app.configs.database import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey


class CreditCardModel(db.Model):
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True)

    expire_date = Column(String, nullable=False)
    number = Column(String, nullable=False, unique=True)
    provider = Column(String(50), nullable=False)
    security_code = Column(String(3))

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("UserModel", backref=backref("credit_cards"), uselist=False)
