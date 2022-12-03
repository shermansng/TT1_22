from sqlalchemy import Column, DECIMAL, Integer, String
from sqlalchemy.dialects.mysql import BIT
from config import db

class BankAccount(db.Model):
    __tablename__ = 'BankAccount'

    AccountID = Column(Integer, primary_key=True, nullable=False)
    UserID = Column(Integer, primary_key=True, nullable=False)
    AccountType = Column(String(255))
    AccountBalance = Column(DECIMAL(10, 2))

    def json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}