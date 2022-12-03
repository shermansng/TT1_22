from config import db
class APITransactionLog(db.Model):

    __tablename__ = "Api_transactions_log"

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String, nullable=True)
    request = db.Column(db.String, nullable=True)
    response = db.Column(db.String, nullable=True)
    uuid = db.Column(db.String, nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)
    # updated_on = db.Column(db.Date, nullable=True)

    def __init__(self, id, service, request, response, uuid, created_on):
        self.id = id
        self.service = service
        self.request = request
        self.response = response
        self.uuid = uuid
        self.created_on = created_on

  