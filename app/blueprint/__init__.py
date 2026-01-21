from .auth import auth_db

def register_all_blueprint(app):
    app.register_blueprint(auth_db, url_prefix='/auth')