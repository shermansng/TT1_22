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


class ScheduledTransaction(db.Model):
    __tablename__ = 'ScheduledTransactions'

    TransactionID = Column(Integer, primary_key=True, nullable=False)
    AccountID = Column(Integer, primary_key=True, nullable=False)
    ReceivingAccountID = Column(Integer)
    Date = Column(String(255))
    TransactionAmount = Column(DECIMAL(10, 2))
    Comment = Column(String(255))

    def json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(db.Model):
    __tablename__ = 'User'

    UserID = Column(Integer, primary_key=True)
    Username = Column(String(20))            
    Password = Column(String(20))
    Firstname = Column(String(255))        
    Lastname = Column(String(255))
    Email = Column(String(255))
    Address = Column(String(255))
    OptIntoPhyStatements = Column(BIT(1)) 

    def json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    
