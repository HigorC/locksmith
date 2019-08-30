from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token)
from flask import json, Flask, jsonify, request
import os

# Armazena a instância de app, para conseguir mudar a secret na criação de tokens
app_global = None

def configure_manager(app):
    app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "secret-to-local-run") 
    global app_global
    app_global  = app
    jwt = JWTManager(app)

def createAccessToken(secret, objIdentity = None):
    app_global.config['JWT_SECRET_KEY'] = secret 
    return create_access_token(identity = objIdentity)

def createRefreshToken(secret):
    app_global.config['JWT_SECRET_KEY'] = secret 
    return create_refresh_token(identity = None)

def authenticateToken(secret):
    # app_global.config['JWT_SECRET_KEY'] = secret 
    # get_jwt_identity()
    try:
        authenticateTokenUsingPrivateSecret()
    except:
        print("An exception occurred")
    authenticateTokenUsingSavedAppSecret("123s")

    return jsonify(authorization = True), 200


# Valida o token utilizando uma secret default da aplicação
def authenticateTokenUsingPrivateSecret():
    app_global.config['JWT_SECRET_KEY'] = "123"
    print(get_jwt_identity())
    # return jsonify(authorization = True), 200

# Valida o token utilizando o secret salvo no banco
def authenticateTokenUsingSavedAppSecret(secret):
    app_global.config['JWT_SECRET_KEY'] = secret 
    get_jwt_identity()
    # return jsonify(authorization = True), 200