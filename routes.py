import os
import app_flask as app_flask
from flask import Blueprint, Flask, request, jsonify
import requests
import managers.jwt_manager as jwt_manager
# from flask_jwt_extended import jwt_required, jwt_refresh_token_required, verify_jwt_in_request
import managers.users as users_manager
import utils.validator as validator
import utils.exception_messages as exception_messages

import jwt
import json

import db.querys as querys

app_blueprint = Blueprint('routes', __name__)

# -------------------------------------------
# Defaults

@app_blueprint.route("/itWorks", methods=['GET'])
def defaultRoute():
    return "Yes, it works without a Token JWT!"

@app_blueprint.route("/teste", methods=['GET'])
def teste():
    return jwt_manager.authenticateToken(1)
    # return "Yteste!"

# -------------------------------------------
# Token

# TODO
# Não passar userID por parâmetro, desse jeito se tiver um token válido posso alterar qualquer outro user
@app_blueprint.route("/user/<userId>/generateToken/<nameApp>", methods=['GET'])
def generateToken(userId, nameApp):

    if users_manager.isUsuarioLogado(request.headers.get("authorization")) is True:
        secret = querys.getSecretByUserIdAndAppName(userId, nameApp)

        response = {
            "access_token": jwt_manager.createComumAccessToken(secret)
        }

        text, status_code = jsonify(response), 201
    else:
        text, status_code = "Necessário fazer login para acessar esta funcionalidade", 400
    
    return text, status_code

# @app_blueprint.route("/refreshToken", methods=['GET'])
# # @jwt_refresh_token_required
# def refreshToken():
#     return jsonify({"access_token": jwt_manager.createAccessToken("123")}), 201

# @jwt_required
@app_blueprint.route("/authenticateToken", methods=['GET'])
def auth():
    json, status_code = jwt_manager.authenticateToken(request.headers.get("authorization"), "123")
    return json, status_code

# -------------------------------------------
# User

@app_blueprint.route("/createUser", methods=['POST'])
def createUser():
    text, status_code = users_manager.createUser(request.json)
    return text, status_code

@app_blueprint.route("/login", methods=['POST'])
def login():
    text, status_code = users_manager.login(request.json)
    return text, status_code

# http://localhost:5000/user/5d68810541e9d5413ece66f2/newApp?name=teste&secret=bombom
@app_blueprint.route("/user/<userId>/newApp", methods=['POST'])
def vinculateApplication(userId):
    if users_manager.isUsuarioLogado(request.headers.get("authorization")) is True:
        text, status_code =  users_manager.vinculateApp(userId, request.args.get("name"), request.args.get("secret"))
    else:
        text, status_code = "Necessário fazer login para acessar esta funcionalidade", 400
    
    return text, status_code