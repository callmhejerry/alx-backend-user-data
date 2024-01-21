#!/usr/bin/env python3
"""
Route api module
"""
from api.v1.views import app_views
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

AUTHENTICATION_TYPE = os.getenv("AUTH_TYPE")

if AUTHENTICATION_TYPE == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTHENTICATION_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before_request():
    """function to call before request
    Returns:
        description
    """
    if auth is None:
        pass
    else:
        excluded_list = ['/api/v1/status/',
                         '/api/v1/unauthorized/', '/api/v1/forbidden/']
        if auth.require_auth(request.path, excluded_list):
            if auth.authorization_header(request) is None:
                abort(401, description="Unauthorized")
            if auth.current_user(request) is None:
                abort(403, description='Forbidden')

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error) -> str:
    """Handle Authorization
    Args:
        error (type): description
    Returns:
        str: description
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> str:
    """Handle all error
    Args:
        error(type): description
    Returns:
        str: description
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
