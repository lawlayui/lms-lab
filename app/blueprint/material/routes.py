from flask import request, jsonify, g
from app.utils.error_handler import safe_route
from .models import read_materail_db, create_course_db
from .forms import ValidationFormsBase
from . import material_bp


@material_bp.route('/course/<int:id>/material', methods=['GET', 'POST'])
@safe_route
def get_material(id):
    if request.method == 'POST':
        data = request.get_json()
        try:
            ValidationFormsBase(title=data['title'], description=['title'])

        except:
            raise ValueError("Key Error")
        return 
    data = read_materail_db(id)
    return jsonify({
        'status': 'succes',
        'materails': data
    })
