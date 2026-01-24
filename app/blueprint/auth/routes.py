from flask import request, jsonify
from app.utils.error_handler import safe_route
from .forms import validation_forms
from .service import user_register, user_login
from . import auth_bp

@auth_bp.route('/register',methods=['POST'])
@safe_route
def register():
    data = request.get_json()
    validation_forms(data)
    token = user_register(data['username'],data['password'], data['role'])
    return jsonify({
        'status':'succes',
        'message':'Successful account creation',
        'token': token
    })

@auth_bp.route('/login',methods=['POST'])
@safe_route
def login():
    data = request.get_json()
    validation_forms(data)
    token =  user_login(data['username'],data['password'])
    return jsonify(
        {
            'status':'succes',
            'message':'succes login',
            'token':token
        }
    )
