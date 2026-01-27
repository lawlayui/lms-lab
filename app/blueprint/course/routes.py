from . import course_bp
from flask import request, jsonify
from app.utils.error_handler import safe_route
from .service import read_course, create_course, courses_taken
from .forms import validation_forms


@course_bp.route('/course/<int:id>')
@safe_route
def course_id(id):
    return jsonify(read_course(id))


@course_bp.route('/course', methods=['POST', 'GET'])
@safe_route
def course():
    if request.method == 'POST':
        data = request.get_json()
        validation_forms(data)
        course_id = create_course(data)
        return jsonify({
            'status': 'succes',
            'course_id': course_id
        })
    return jsonify(courses_taken())
