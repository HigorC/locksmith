from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from flask import Flask, jsonify, request
import os

def configure_manager(app):
    app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "secret-to-local-run") 
    jwt = JWTManager(app)

def create(object_to_put):
    access_token = create_access_token(identity=object_to_put)
    return jsonify(access_token=access_token), 201

def get_identity_object_from_token():
    current_object = get_jwt_identity() or {}
    return current_object, 200