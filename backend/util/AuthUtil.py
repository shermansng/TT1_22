from models.BlacklistToken import BlacklistToken
from config import db, app
import datetime
import jwt


class AuthUtil():
    def getAuthToken(request):
        """
        Get Auth token from header 
        :return: string|None
        """
        auth_header = request.headers.get('Authorization')
        auth_token = None
        if auth_header:
            auth_token = auth_header.split(" ")[1]
       
        return auth_token

    def checkBlacklistToken(token):
        """
        Check Auth token exist inside blacklist token table
        :return: blacklistToken|None
        """
        blacklist_token = BlacklistToken.query.filter_by(token=token).first()
        return blacklist_token

    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e    

    def encode_auth_token_days(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e    

    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: string|boolean
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            # return payload['sub']
            return True
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'