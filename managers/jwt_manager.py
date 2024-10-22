from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from flask import json, Flask, jsonify, request
import os

def configure_manager(app):
    app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "secret-to-local-run") 
    jwt = JWTManager(app)

def createToken():
    return create_access_token(identity = None)

def auth():
    get_jwt_identity()
    return jsonify(authorization = True), 200