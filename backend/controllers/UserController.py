from models.User import User
from flask_bcrypt import Bcrypt
from flask import jsonify
from uuid import uuid4
from config import app, db
from util.AuthUtil import AuthUtil


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
                        return jsonify({
                            "code": 200,
                            "data": {
                                "status": "success",
                                "id": user_data.UserID,
                                "firstName": user_data.Firstname,
                                "lastName": user_data.Lastname,
                                "token": auth_token.decode("utf-8")
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
                        }),404

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

    def updateUserDetails(request):
        data = request.get_json()
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
            
