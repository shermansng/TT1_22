import config
from controllers.UserController import UserController
from controllers.TransactionController import TransactionController
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from util.APITransactionLogUtil import APITransactionLogUtil
from uuid import uuid4

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


#get transactions by bank account id
@app.route("/transactions/byAccount" , methods=["POST"])
def getTransactionsByAccount():
    uuid = str(uuid4())
    APITransactionLogUtil.insertLog("GET Transactions", request.get_json(), None, uuid)
    response = TransactionController.getTransactionsByAccount(request)
    # APITransactionLogUtil.insertLog("User Auth", request.get_data(), response.get_data(), uuid)
    return response

@app.route("/user/login", methods=["POST"])
def authUser():
    uuid = str(uuid4())
    APITransactionLogUtil.insertLog("User Auth", request.get_json(), None, uuid)
    response = UserController.authUser(request)
    # APITransactionLogUtil.insertLog("User Auth", request.get_data(), response.get_data(), uuid)
    return response

@app.route("/user/info", methods=["POST"])
def retrieveUserDetails():
    uuid = str(uuid4())
    APITransactionLogUtil.insertLog("User Info", request.get_json(), None, uuid)
    response = UserController.retrieveUserDetails(request)
    # APITransactionLogUtil.insertLog("User Info", request.get_data(), response.get_data(), uuid)
    return response

@app.route("/user/updateInfo", methods=["POST"])
def updateUserDetails():
    uuid = str(uuid4())
    APITransactionLogUtil.insertLog("UPDATE User Info", request.get_json(), None, uuid)
    response = UserController.updateUserDetails(request)
    # APITransactionLogUtil.insertLog("UPDATE User Info", request.get_data(), response.get_data(), uuid)
    return response

@app.route("/user/logout", methods=["POST"])
def logoutUser():
    uuid = str(uuid4())
    APITransactionLogUtil.insertLog("LOGOUT", None, None, uuid)
    response = UserController.logoutUser(request)
    return response

@app.route("/user/bankaccounts", methods=["POST"])
def getBankAccInfo():
    uuid = str(uuid4())
    APITransactionLogUtil.insertLog("Get Bank Account Info", request.get_json(), None, uuid)
    response = UserController.getBankAccInfo(request)
    # APITransactionLogUtil.insertLog("Get Bank Account Info", request.get_data(), response.get_data(), uuid)
    return response

#insert transaction by 
@app.route("/transactions/insert", methods=['POST'])
def insertTransaction():
     return TransactionController.insert_transaction(request)

#delete transaction by 
@app.route("/transactions/delete", methods=['GET', 'DELETE'])
def deleteTransaction():
     return TransactionController.delete_Transaction(request)

@app.route("/user/accountid", methods=["POST"])
def getAccountId():
    uuid = str(uuid4())
    APITransactionLogUtil.insertLog("Get account id info", request.get_json(), None, uuid)
    response = UserController.getAccountId(request)
    # APITransactionLogUtil.insertLog("Get Bank Account Info", request.get_data(), response.get_data(), uuid)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)