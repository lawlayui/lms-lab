from . import course_bp
from flask import request, jsonify, g
from app.utils.error_handler import safe_route
from .service import read_course, create_course, courses_taken
from .forms import validation_forms
from .models import delete_course_db, leave_course_db


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


@course_bp.route('/course/<int:id>/delete', methods=['GET'])
@safe_route
def course_delete(id):
    delete_course_db(id)
    role = g.dataUser['role']
    if role == 'student':
        return jsonify({
            "status": "Students cannot delete courses"
        })
    return jsonify({
        "status": "Succes"
    })


@course_bp.route('/course/<int:id>/leave', methods=['GET'])
@safe_route
def course_leave(id):
    leave_course_db(id)
    return jsonify({
        "status": "succes"
    })
