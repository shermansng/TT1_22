from flask import Flask, request, jsonify
from config import app, db
from models.ScheduledTransaction import ScheduledTransaction

class TransactionController():
    def getTransactionsByAccount(request):

        data = request.get_json()
        try:
            transactionList = ScheduledTransaction.query.filter(ScheduledTransaction.AccountID == data["accountID"]).all()
            result = [e.json() for e in transactionList]

            if len(transactionList):
                result = [e.json() for e in transactionList]
                return jsonify(
                        {
                            "code": 200,
                            "data": result
                        }
                    ),200; 
            else:
                return jsonify(
                {
                    "code": 400,
                    "data": "no transactions found"
                }
            )

        except Exception as error: 
            print(error)
            return jsonify(
                {
                    "code": 400,
                    "data": "Data format error"
                }
            ),400

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
            numOfDeletedTransactions = 0

            if len(data) > 0:
                for i in data["transactionID"]:
                    transaction = ScheduledTransaction.query.filter_by(TransactionID=i).first()
                    if transaction != None:
                        db.session.delete(transaction)
                        db.session.commit()
                        numOfDeletedTransactions += 1
                        
                if(numOfDeletedTransactions > 0):
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