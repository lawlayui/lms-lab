from flask import request, jsonify, g
from app.utils.error_handler import safe_route
from .models import read_materail_db, create_material_db
from .forms import ValidationFormsBase
from . import material_bp


@material_bp.route('/course/<int:id>/material', methods=['GET', 'POST'])
@safe_route
def get_material(id):
    if request.method == 'POST':
        data = request.get_json()
        ValidationFormsBase(title=data['title'], description=data['description'])
        create_material_db(data['title'], data['description'], id)
        return jsonify(
            {
                'status': 'succes'
            }
        )
    data = read_materail_db(id)
    return jsonify({
        'status': 'succes',
        'materails': data
    })
