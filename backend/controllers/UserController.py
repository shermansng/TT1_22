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
                    print(user_data)    
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
            
