from functools import wraps
from flask import current_app, jsonify 
import traceback

def safe_route(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return jsonify({
                'status':'error',
                'messsage':str(e)
            }), 400
        except Exception as e:
            current_app.logger.error(traceback.format_exc())
            return jsonify({
                'status':'error',
                'message':'internal server error'
            }), 500
    return wrapper