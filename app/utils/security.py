import jwt 
import datetime 
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

def generate_hash(password: str):
    password_hashed = generate_password_hash(password)
    return password_hashed

def verify_hash(password: str, password_hash: str):
    result = check_password_hash(password_hash,password)
    if result:
        return True
            
    raise ValueError("Invalid password")

def generate_jwt(data: dict):
    payload = {
        'exp':datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(weeks=52),
        'iat':datetime.datetime.now(datetime.timezone.utc),
        'data': data
    }
    token = jwt.encode(payload,current_app.config['SECRET_KEY'],algorithm='HS256')
    return token.decode("utf-8")

def verify_token(token: str):
    result = jwt.decode(token,current_app.config['SECRET_KEY'],algorithms=['HS256'])
    return result 