from models.User import User
from models.BankAccount import BankAccount
from flask_bcrypt import Bcrypt
from flask import jsonify
from uuid import uuid4
from config import app, db
from util.AuthUtil import AuthUtil
from models.BlacklistToken import BlacklistToken


bcrypt = Bcrypt(app)

class UserController():
    def authUser(request):
        data = request.get_json()
        try:
            if len(data) > 0:
                try:
                    user_data = User.query.filter_by(Username=data["username"]).first()
                  
                    if user_data == None:
                        return jsonify({
                            "code": 404,
                            "data": {
                                "status": "fail",
                                "message": "User not found"
                            }
                        })

                    if user_data.Password == data["password"]:
                        auth_token = AuthUtil.encode_auth_token(user_data.Email)
                        if user_data.LoginCount > 4:
                            user_data.LoginCount = 0
                            db.session.commit()
                        else:
                            user_data.LoginCount += 1
                            db.session.commit()

                        return jsonify({
                            "code": 200,
                            "data": {
                                "status": "success",
                                "id": user_data.UserID,
                                "firstName": user_data.Firstname,
                                "lastName": user_data.Lastname,
                                "token": auth_token.decode("utf-8"),
                                "loginCount": user_data.LoginCount
                            }
                        })
                    else:
                        return jsonify({
                            "code": 200,
                            "data": {
                                "status": "fail",
                                "message": "Invalid password"
                            }
                        })
                    
                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "User Auth error. Please contact the administrator"
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

    def retrieveUserDetails(request):
        data = request.get_json()

        auth_token = AuthUtil.getAuthToken(request)
        existingBlacklistToken = AuthUtil.checkBlacklistToken(auth_token)
        if auth_token != None:
            if existingBlacklistToken == None:
                resp = AuthUtil.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    try:
                        if len(data) > 0:
                            try:
                                user_data = User.query.filter_by(UserID=data["id"]).first()
                                print(user_data)    
                                if user_data == None:
                                    return jsonify({
                                        "code": 404,
                                        "data": {
                                            "status": "fail",
                                            "message": "User details not found"
                                        }
                                    })

                                else:
                                    return jsonify({
                                            "code": 200,
                                            "data": {
                                                "firstName": user_data.Firstname,
                                                "lastName": user_data.Lastname,
                                                "email": user_data.Email,
                                                "address": user_data.Address,
                                                "optIntoPhyStatements": user_data.OptIntoPhyStatements

                                            }
                                        })
                                
                            except Exception as error:
                                print(error)
                                return jsonify(
                                    {
                                        "code": 500,
                                        "data": "Retreive User info error. Please contact the administrator"
                                    }
                                ),500
                    except Exception as error:
                        print(error)
                        return jsonify(
                            {
                                "code": 400,
                                "data": "Data format error"
                            }
                        ),400
                else:
                    responseObject = {
                        'status': 'fail',
                        'message': resp
                    }
                    return (jsonify(responseObject)), 401
            else:
                responseObject = {
                        'status': 'fail',
                        'message': 'Invalid Token'
                    }
                return (jsonify(responseObject)), 401
        else:
            responseObject = {
                "code": 401,
                'message': 'Provide a valid auth token'
            }
            return (jsonify(responseObject)), 401

        

    def updateUserDetails(request):
        data = request.get_json()

        auth_token = AuthUtil.getAuthToken(request)
        existingBlacklistToken = AuthUtil.checkBlacklistToken(auth_token)
        if auth_token != None:
            if existingBlacklistToken == None:
                resp = AuthUtil.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    try:
                        if len(data) > 0:
                            try:
                                user_data = User.query.filter_by(UserID=data["id"]).first()
                                
                                if user_data == None:
                                    return jsonify({
                                        "code": 404,
                                        "data": {
                                            "status": "fail",
                                            "message": "User details not found"
                                        }
                                    }),404

                                else:
                                    if(len(data["email"]) == 0 and len(data["address"]) == 0):
                                        return jsonify({
                                            "code": 200,
                                            "data": {
                                                "status": "fail",
                                                "message": "No data is updated"
                                            }
                                        }),200
                                    else:

                                        if(len(data["email"]) != 0):
                                            user_data.Email = data["email"]
                                        if(len(data["address"]) != 0):
                                            user_data.Address = data["address"]
                                        db.session.commit()
                                        return jsonify({
                                            "code": 200,
                                            "data": {
                                                "status": "success"
                                            }
                                        }),200
                                
                            except Exception as error:
                                print(error)
                                return jsonify(
                                    {
                                        "code": 500,
                                        "data": "User Update Info Error. Please contact the administrator"
                                    }
                                ),500
                    except Exception as error:
                        print(error)
                        return jsonify(
                            {
                                "code": 400,
                                "data": "Data format error"
                            }
                        ),400
                else:
                    responseObject = {
                        'status': 'fail',
                        'message': resp
                    }
                    return (jsonify(responseObject)), 401
            else:
                responseObject = {
                        'status': 'fail',
                        'message': 'Invalid Token'
                    }
                return (jsonify(responseObject)), 401
        else:
            responseObject = {
                "code": 401,
                'message': 'Provide a valid auth token'
            }
            return (jsonify(responseObject)), 401
        

    def logoutUser(request):
        auth_token = AuthUtil.getAuthToken(request)
        existingBlacklistToken = AuthUtil.checkBlacklistToken(auth_token)
        if auth_token != None:
            if existingBlacklistToken == None:
                resp = AuthUtil.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    # mark the token as blacklisted
                    blacklist_token = BlacklistToken(token=auth_token)
                    try:
                        # insert the token
                        db.session.add(blacklist_token)
                        db.session.commit()
                        responseObject = {
                            "code": 200,
                            'status': 'success',
                            'message': 'Successfully logged out.'
                        }
                        return (jsonify(responseObject)), 200
                    except Exception as e:
                        responseObject = {
                            "code": 401,
                            'status': 'fail',
                            'message': e
                        }
                        return (jsonify(responseObject)), 200
                else:
                    responseObject = {
                        "code": 401,
                        'status': 'fail',
                        'message': resp
                    }
                    return (jsonify(responseObject)), 200
            else:
                responseObject = {
                        "code": 401,
                        'status': 'fail',
                        'message': 'Invalid Token'
                    }
                return (jsonify(responseObject)), 200

        else:
            return jsonify(
                {
                    "code": 401,
                    "data": "Provide a valid auth token"
                }
            ), 200
            
    def getBankAccInfo(request):
        # Receive the userid from the request
        data = request.get_json()

        auth_token = AuthUtil.getAuthToken(request)
        existingBlacklistToken = AuthUtil.checkBlacklistToken(auth_token)
        if auth_token != None:
            if existingBlacklistToken == None:
                resp = AuthUtil.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    try:
                        # Retrieve the user data according to userid from BankAccount Table
                        # Include query within try block to catch any errors
                        user_bank_acc_data = BankAccount.query.filter_by(UserID=data["userid"]).all()

                        # if userid returns empty list, it means the user does not exist, return 404
                        if user_bank_acc_data == []:
                            return jsonify({
                                "code": 404,
                                "data": {
                                    "status": "failure",
                                    "message": "User does not exist"
                                }
                            })

                        # if userid returns a pupolated list, it means the user exists, return 200 and data retrieved
                        else:
                            bank_acc_data = []
                            
                            for bank_acc in user_bank_acc_data:
                                bank_acc_data.append(bank_acc.json())

                            return jsonify({
                                "code": 200,
                                "status": "success",
                                "message": "User bank account successfully retrieved",
                                "data": bank_acc_data
                                
                            })
                
                    # catch any request error and return 500
                    except Exception as error:
                        print(error)
                        return jsonify(
                            {
                                "code": 500,
                                "data": "Please check your POST request values"
                            }
                        ),500
                else:
                    responseObject = {
                        'status': 'fail',
                        'message': resp
                    }
                    return (jsonify(responseObject)), 401
            else:
                responseObject = {
                        'status': 'fail',
                        'message': 'Invalid Token'
                    }
                return (jsonify(responseObject)), 401
        else:
            responseObject = {
                "code": 401,
                'message': 'Provide a valid auth token'
            }
            return (jsonify(responseObject)), 401

       
    
    def getAccountId(request):
        # Receive the userid from the request
        data = request.get_json()

        auth_token = AuthUtil.getAuthToken(request)
        existingBlacklistToken = AuthUtil.checkBlacklistToken(auth_token)
        if auth_token != None:
            if existingBlacklistToken == None:
                resp = AuthUtil.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    try:
                        # Retrieve Account ID(s) according to userid from BankAccount Table
                        # Include query within try block to catch any errors
                        user_acc_id_data = BankAccount.query.filter_by(UserID=data["userid"]).all()

                        # if userid returns empty list, it means the user does not exist, return 404
                        if user_acc_id_data == []:
                            return jsonify({
                                "code": 404,
                                "data": {
                                    "status": "failure",
                                    "message": "User does not exist"
                                }
                            })

                        # if userid returns a pupolated list, it means the user exists, return 200 and data retrieved
                        else:
                            acc_id_data = []
                            
                            for bank_acc in user_acc_id_data:
                                acc_id_data.append(bank_acc.AccountID)

                            return jsonify({
                                "code": 200,
                                "status": "success",
                                "message": "User Account ID successfully retrieved",
                                "data": acc_id_data
                                
                            })
                    
                    # catch any request error and return 500
                    except Exception as error:
                        print(error)
                        return jsonify(
                            {
                                "code": 500,
                                "data": "Please check your POST request values"
                            }
                        ),500
                else:
                    responseObject = {
                        'status': 'fail',
                        'message': resp
                    }
                    return (jsonify(responseObject)), 401
            else:
                responseObject = {
                        'status': 'fail',
                        'message': 'Invalid Token'
                    }
                return (jsonify(responseObject)), 401
        else:
            responseObject = {
                "code": 401,
                'message': 'Provide a valid auth token'
            }
            return (jsonify(responseObject)), 401

    