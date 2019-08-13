import os
import app_flask as app_flask
from flask import Blueprint, Flask, request, jsonify
import managers.jwt as jwt_manager
from flask_jwt_extended import jwt_required
 
app_blueprint = Blueprint('routes', __name__)

@app_blueprint.route("/itWorks")
def defaultRoute():
    return "Yes, it works!"

@app_blueprint.route("/create", methods=['POST'])
def create():
    return jwt_manager.create(request.json)

@app_blueprint.route("/auth")
@jwt_required
def auth():
    return jwt_manager.get_identity_object_from_token()