from .auth import auth_bp
from .test import test_bp
def register_all_blueprint(app):
    app.register_blueprint(test_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')