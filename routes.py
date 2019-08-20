import os
import app_flask as app_flask
from flask import Blueprint, Flask, request, jsonify
import requests
import managers.jwt_manager as jwt_manager
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
import managers.users as users_manager
import utils.validator as validator
import utils.exception_messages as exception_messages

app_blueprint = Blueprint('routes', __name__)

# Defaults

@app_blueprint.route("/itWorks", methods=['GET'])
def defaultRoute():
    return "Yes, it works without a Token JWT!"

@app_blueprint.route("/itWorksWithToken", methods=['GET'])
@jwt_required
def defaultRouteWithToken():
    return "Yes, it works with Token JWT!"

# Token

@app_blueprint.route("/generateToken", methods=['GET'])
@jwt_required
def generateToken():

    token = request.headers.get("authorization")
    
    if validator.isUserLogged(token) is False:
        return exception_messages.getMsgLoginRequerido(), 400

    response = {
        "access_token": jwt_manager.createAccessToken(),
        "refresh_token": jwt_manager.createRefreshToken()
    }

    return jsonify(response), 201

@app_blueprint.route("/refreshToken", methods=['GET'])
@jwt_refresh_token_required
def refreshToken():
    return jsonify({"access_token": jwt_manager.createAccessToken()}), 201

@app_blueprint.route("/authenticateToken", methods=['GET'])
@jwt_required
def auth():
    json, status_code = jwt_manager.authenticateToken()
    return json, status_code

# User

@app_blueprint.route("/createUser", methods=['POST'])
def createUser():
    text, status_code = users_manager.createUser(request.json)
    return text, status_code

@app_blueprint.route("/login", methods=['POST'])
def login():
    text, status_code = users_manager.login(request.json)
    return text, status_code

@app_blueprint.route("/user/<userId>/newApp", methods=['GET'])
def vinculateApplication(userId):
    print(userId)
    print(request.args.get("name"))

    users_manager.vinculateApp(userId, request.args.get("name"), request.args.get("secret"))
    return 'oi'