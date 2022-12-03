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

#get transaction by 
@app.route("/transactions")
def getTransaction():
    return TransactionController.getTransaction(request)
    
@app.route("/user/login", methods=["POST"])
def authUser():
    return UserController.authUser(request)

@app.route("/user/info", methods=["POST"])
def retrieveUserDetails():
    return UserController.retrieveUserDetails(request)

@app.route("/user/updateInfo", methods=["POST"])
def updateUserDetails():
    return UserController.updateUserDetails(request)

@app.route("/user/bankaccounts", methods=["POST"])
def getBankAccInfo():
    return UserController.getBankAccInfo(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)