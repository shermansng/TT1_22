import config
from controllers.UserController import UserController
from controllers.TransactionController import TransactionController
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS


app = config.app
CORS(app)

@app.route("/monitoring")
def test_api():
    return jsonify(
        {
            "code": 200,
            "data": "API monitoring is working"
        }
    )

#get all transactions
@app.route("/transactions" , methods=["GET"])
def getTransaction():
     return TransactionController.getTransaction(request)

#get transactions by bank account id
@app.route("/transactionsByAccount" , methods=["POST"])
def getTransactionsByAccount():
     return TransactionController.getTransactionsByAccount(request)


    
@app.route("/user/login", methods=["POST"])
def authUser():
    return UserController.authUser(request)

@app.route("/user/info", methods=["POST"])
def retrieveUserDetails():
    return UserController.retrieveUserDetails(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)