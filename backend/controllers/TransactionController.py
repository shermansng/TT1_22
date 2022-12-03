from flask import Flask, request, jsonify
from models.ScheduledTransaction import ScheduledTransaction

class TransactionController():

    def getTransactionsByAccount(request):
        data = request.get_json()
        try:
            transactionList = ScheduledTransaction.query.filter(ScheduledTransaction.AccountID == data["accountID"]).all()
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
                    "code": 500,
                    "data": "Data format error"
                }
            )

        
        


