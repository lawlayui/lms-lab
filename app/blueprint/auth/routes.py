from flask import request, jsonify
from app.utils.error_handler import safe_route
from .forms import validation_forms
from . import auth_bp

@auth_bp.route('/register',methods=['POST'])
@safe_route
def register():
    data = request.get_json()
    validation_forms(data)

