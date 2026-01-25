from .auth import auth_bp
from .test import test_bp
from .course import course_bp
def register_all_blueprint(app):
    app.register_blueprint(course_bp, url_prefix='/api')
    app.register_blueprint(test_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api')