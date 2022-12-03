from sqlalchemy import Column, DECIMAL, Integer, String
from sqlalchemy.dialects.mysql import BIT
from config import db


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