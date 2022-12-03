from config import db

class User(db.Model):
    __tablename__ = "User"

    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String, nullable=True)
    Password = db.Column(db.String, nullable=True)
    Firstname = db.Column(db.String, nullable=True)
    Lastname = db.Column(db.String, nullable=True)
    Email = db.Column(db.String, nullable=True)
    Address = db.Column(db.String, nullable=True)
    OptIntoPhyStatements = db.Column(db.String, nullable=True)
    
    def __init__(self, UserID, Username, Password, Firstname, Lastname, Email, Address, OptIntoPhyStatements):
        self.UserID = UserID
        self.Username = Username
        self.Password = Password
        self.Firstname = Firstname
        self.Lastname - Lastname
        self.Email = Email
        self.Address = Address
        self.OptIntoPhyStatements = OptIntoPhyStatements

    
