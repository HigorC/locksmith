from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token)
from flask import json, Flask, jsonify, request
import os

def configure_manager(app):
    app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "secret-to-local-run") 
    jwt = JWTManager(app)

def createAccessToken():
    return create_access_token(identity = None)

def createRefreshToken():
    return create_refresh_token(identity = None)

def authenticateToken():
    get_jwt_identity()
    return jsonify(authorization = True), 200