from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token,
    decode_token)
from flask import json, Flask, jsonify, request
import os

import jwt

# Armazena a instância de app, para conseguir mudar a secret na criação de tokens
# app_global = None

# def configure_manager(app):
    # app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "secret-to-local-run") 
    # global app_global
    # app_global  = app
    # jwt = JWTManager(app)

def createComumAccessToken(secret, objIdentity = None):
    token = jwt.encode(objIdentity, secret, algorithm='HS256')
    return token.decode("utf-8")

# Não deve ser mapeado nas rotas, uso privado
def createAdminAccessToken():
    token = jwt.encode({}, "admin", algorithm='HS256')
    return token.decode("utf-8")

def createRefreshToken(secret):
    app_global.config['JWT_SECRET_KEY'] = secret 
    return create_refresh_token(identity = None)

def authenticateToken(token, secret):
    print(">> Validando assinatura do Token...")
    try:
        # VERIFICAR SE É UM TOKEN PROPRIO, SECRET APENAS LOCAL
        jwt.decode(token, "admin", algorithms='HS256')
        print(">> Token de ADMIN verificado!")
        return jsonify({"authorization": True, "admin": True}), 200
    except jwt.exceptions.InvalidSignatureError:
        # TENTA COM OUTRA SECRET
        try:
            print(">> O Token não é de ADMIN. Tentando com o secret passado...")
            jwt.decode(token, secret, algorithms='HS256')
            print(">> Token verificado!")
            return jsonify({
                "authorization": True,
                "admin": False
            }), 200
        except jwt.exceptions.InvalidSignatureError:
            print("[X] >> A Assinatura do Token é inválida.")
            return "A Assinatura do Token é inválida.", 400
        except jwt.exceptions.ExpiredSignatureError:
            print("[X] >> O Token expirou.")
            return "O Token expirou.", 400
    except jwt.exceptions.ExpiredSignatureError:
        print("[X] >> O Token expirou.")
        return "O Token expirou.", 400

def decodeToken(token, secret):
    # app_global.config['JWT_SECRET_KEY'] = secret 
    # get_jwt_identity()
    # print("#########")
    # print(decode_token(request.headers.get("authorization")))

   

    try:
        decoded = jwt.decode(token, secret, algorithms='HS256')
    except jwt.exceptions.InvalidSignatureError:
        print("ass invalida")

    # try:
    #     authenticateTokenUsingPrivateSecret()
    # except:
    #     print("An exception occurred")
    # authenticateTokenUsingSavedAppSecret("123s")

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