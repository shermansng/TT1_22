import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

# DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost:3306/testing'
# SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('SECRET_KEY')

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/testing'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://techtrek_admin:techtrekSb2746oqwJ3QzX@techtrek-mysql.c9yrvpifl3ul.ap-southeast-1.rds.amazonaws.com:3306/testing'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.environ.get('DATABASE_URL')}/{os.environ.get('DATABASE_NAME')}"
# username:password@host:port/database
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)





