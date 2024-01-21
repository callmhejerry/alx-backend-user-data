#!/usr/bin/env python3
"""Index view Module
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """Handle authorization
    Returns:
        str: description
    """
    abort(401, description='Unauthorized')

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """Handle forbidden
    Returns:
        str: description
    """
    abort(403, description='Forbidden')


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - total objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
