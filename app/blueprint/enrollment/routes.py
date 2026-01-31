from . import enrollment_bp
from flask import request, jsonify
from app.utils.error_handler import safe_route
from .service import create_enrollment


@enrollment_bp.route('/course/<int:id>/enrollment', methods=['GET'])
@safe_route
def enrollment(id):
    create_enrollment(id)
    return jsonify(
        {
            "message": "succes enrollment"
        }
    ) 
