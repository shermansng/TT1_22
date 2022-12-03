from flask import Flask, request, jsonify
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

