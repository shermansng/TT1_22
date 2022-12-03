from models.User import User
from flask_bcrypt import Bcrypt
from flask import jsonify
from uuid import uuid4
from config import app, db
from models.BlacklistToken import BlacklistToken
from util.AuthUtil import AuthUtil


bcrypt = Bcrypt(app)

class UserController():
    pass