from config import db
from models.APITransactionLog import APITransactionLog
import json
from sqlalchemy.sql import func


class APITransactionLogUtil():
    def insertLog(service_name, request, response, uuid):
        """
        Insert API transaction Log into table
        """
        try:
            request = request.decode('utf-8')
            if(response != None):
                response = response.decode('utf-8')
            else:
                response = None

            insertAPITransaction = APITransactionLog(None, service_name, request, response, uuid, func.now())
            db.session.add(insertAPITransaction)
            db.session.commit()
            # print(insertAPITransaction.id) #return the primary key
        except Exception as error:
            print(error)
            