from flask import Flask, request, jsonify, url_for
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
                # transactionID =  #leave as nan value to be auto populated 
                userID = data["userID"]
                accountID =  data["accountID"] 
                receivingaccountID = data['receivingaccountID'] 
                date =  data['date'] 
                transactionamount = data['transactionamount'] 
                comment = data['comment'] 

                scheduledtransaction = ScheduledTransaction(TransactionID = transactionID , AccountID = accountID, ReceivingAccountID = receivingaccountID,
                                                            Date = date, TransactionAmount=transactionamount, Comment=comment)
                #add transaction to db
                app.db.session.add(scheduledtransaction)     
                app.db.commit()                        
            return jsonify({
                        "code": 200,
                        "data": {
                            "transactionID":scheduledtransaction.TransactionID,
                            "accountID ":  scheduledtransaction.accountID,
                            "receivingaccountID": scheduledtransaction.receivingaccountID,
                            "date":scheduledtransaction.date,
                            "transactionamount":scheduledtransaction.transactionamount,
                            "comment":scheduledtransaction.comment
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

    def delete(request): 
        data = request.get_json()
        try:
            if len(data) > 0:
                transaction = ScheduledTransaction.query.filter_by(data[transaction_id])
                if transaction == None:
                                return jsonify({
                                    "code": 404,
                                    "data": {
                                        "status": "fail",
                                        "message": "Transaction not found"
                                    }
                                }),404
                else: 
                    app.db.session.delete(transaction)
                    app.db.session.commit()
                data 
            return redirect(url_for('getTransaction'))
        except Exception as error: 
            print(error)
            return jsonify(
                {
                    "code": 400,
                    "data": "Data format error"
                }
            ),400