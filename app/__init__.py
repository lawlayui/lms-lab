from flask import Flask, request, g
from .config import Config
from .utils.db import close_db
from .blueprint import register_all_blueprint
from app.utils.error_handler import safe_route
from app.utils.security import verify_token
import datetime
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.teardown_appcontext(close_db)
    register_all_blueprint(app)

    users_ip = {}

    @app.before_request
    @safe_route
    def rate_limiting():
        time_now = datetime.datetime.now(datetime.timezone.utc)
        five_minutes_earlier = time_now - datetime.timedelta(minutes=5)
        ip_user = request.remote_addr
        if request.remote_addr not in users_ip:
            users_ip[ip_user] = []

        users_ip[ip_user] = [time for time in users_ip[ip_user] if time >= five_minutes_earlier]

        users_ip[ip_user].append(time_now)

        if len(users_ip[ip_user]) >= 5:
            raise ValueError("Too much demand")
        
    @app.before_request
    @safe_route
    def read_token():
        free_route = ['auth.register','auth.login']
        target = request.endpoint
        auth_header = request.headers.get('Authorization')
        token = None

        if target == 'static' or target == 'options' or target in free_route:
            return None

        if target not in free_route:
            if auth_header:
                token = auth_header.split(" ")[-1]
                data = verify_token(token)['data']
                g.dataUser = data
                return None
            raise ValueError("Missing token")
        
    return app