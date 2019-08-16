import os
import app_flask as app_flask
from flask import Blueprint, Flask, request, jsonify
import requests
import managers.jwt_manager as jwt_manager
from flask_jwt_extended import jwt_required
import managers.users as users_manager

app_blueprint = Blueprint('routes', __name__)

@app_blueprint.route("/itWorks", methods=['GET'])
def defaultRoute():
    return "Yes, it works!"

@app_blueprint.route("/createToken", methods=['GET'])
def createToken():
    return jsonify(access_token = jwt_manager.createToken()), 201

# TODO
# Corrigir resposta desta rota, retornar sempre o status code neste modulo
@app_blueprint.route("/auth", methods=['GET'])
@jwt_required
def auth():
    return jwt_manager.auth()

@app_blueprint.route("/createUser", methods=['POST'])
def createUser():
    text, status_code = users_manager.createUser(request.json)
    return text, status_code