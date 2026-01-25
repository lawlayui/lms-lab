from . import course_bp 
from flask import request, jsonify
from app.utils.error_handler import safe_route
from .service import get_information_course

@course_bp.route('/course/<id>')
@safe_route
def index(id):
    return get_information_course(id)