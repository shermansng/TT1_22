from sqlalchemy import Column, DECIMAL, Integer, String
from sqlalchemy.dialects.mysql import BIT
from config import db


class ScheduledTransaction(db.Model):
    __tablename__ = 'ScheduledTransactions'

    TransactionID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    AccountID = Column(Integer, primary_key=True, nullable=False)
    ReceivingAccountID = Column(Integer)
    Date = Column(String(255))
    TransactionAmount = Column(DECIMAL(10, 2))
    Comment = Column(String(255))

    def json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}