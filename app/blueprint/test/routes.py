from flask import jsonify 
from . import test_bp

@test_bp.route('/test')
def test():
    return jsonify({'message':'succes'})