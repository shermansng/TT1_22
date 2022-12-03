from flask import Flask, request, jsonify
from config import app, db
from models.ScheduledTransaction import ScheduledTransaction

class TransactionController():
    def getTransaction(request):

        if request.method == "GET":
                
            try:
                transactionList = ScheduledTransaction.query.all()
                result = [e.json() for e in transactionList]
                return jsonify(
                    {
                        "data": result
                    }
                ),200; 
            except Exception as error:
                print(error)
                return jsonify(
                    {
                        "code": 500,
                        "data": "Data format error"
                    }
                )

    def insert_transaction(request): 
        data = request.get_json()
        try:
            if len(data) > 0:
                userID = data["userID"]
                accountID =  data["accountID"] 
                receivingaccountID = data['receivingaccountID'] 
                date =  data['date'] 
                transactionamount = data['transactionamount'] 
                comment = data['comment'] 

                #query and match 


                #adding instance
                scheduledtransaction = ScheduledTransaction(AccountID = accountID, ReceivingAccountID = receivingaccountID,
                                                            Date = date, TransactionAmount=transactionamount, Comment=comment)

                #add transaction to db
                db.session.add(scheduledtransaction)     
                db.session.commit()                        
                return jsonify({
                    "code": 200,
                    "data": {
                        "transactionID":scheduledtransaction.TransactionID,
                        "accountID ":  scheduledtransaction.AccountID,
                        "receivingaccountID": scheduledtransaction.ReceivingAccountID,
                        "date":scheduledtransaction.Date,
                        "transactionamount":scheduledtransaction.TransactionAmount,
                        "comment":scheduledtransaction.Comment
                    }
                })
        except Exception as error: 
            print(error)
            return jsonify(
                {
                    "code": 400,
                    "data": "Data format error"
                }
            ),400

    def delete_Transaction(request): 
        data = request.get_json()
        try:
            if len(data) > 0:
                for i in data["transactionID"]:
                    transaction = ScheduledTransaction.query.filter_by(TransactionID=i).first()
                    if transaction != None:
                        db.session.delete(transaction)
                        db.session.commit()
                    
                        return jsonify({
                            "code": 200,
                            "data": {
                                "message": "Deleted Successfully"
                            }
                        })
                    else:
                        return jsonify({
                            "code": 200,
                            "data": {
                                "message": "No transactions deleted"
                            }
                        })

        except Exception as error: 
            print(error)
            return jsonify(
                {
                    "code": 400,
                    "data": "Data format error"
                }
            ),400