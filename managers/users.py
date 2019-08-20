import requests
import json
import managers.jwt_manager as jwt_manager
import os
import utils.validator as validator
import db.mongo_connection as mongo_connection

def login(jsonFromRequest = {}):
    # TODO 
    # A VALIDAÇÃO DO LOGIN É DIFERENTE, POIS PODE-SE LOGAR COM USER OU EMAIL
    validator.validateRequest(jsonFromRequest)

    print(">> Usuário validado!")

    jsonProntoParaEnvio = {
        "user": jsonFromRequest,
        "application": "locksmith"
    }

    headers = {
        'Authorization': 'Bearer ' + jwt_manager.createAccessToken(),
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    # TODO
    # SETAR A VARIAVEL ABAIXO NAS ENVIROMENTS DO HEROKU 
    url_loginme_login_user = os.environ.get("URL_LOGINME_LOGIN_USER", "http://localhost:5001/login")

    r = requests.post(url_loginme_login_user, data = json.dumps(jsonProntoParaEnvio), headers = headers)

    if str (r.status_code)[0] != "2":
        print("[X] >> Ocorreu um erro no Log-in-me")
        return r.text, r.status_code
    
    return r.text, 200

def createUser(jsonFromRequest = {}):
    validator.validateRequest(jsonFromRequest)

    print(">> Usuário validado!")

    jsonProntoParaEnvio = {
        "user": jsonFromRequest,
        "application": "locksmith"
    }
    
    headers = {
        'Authorization': "Bearer " + jwt_manager.createAccessToken(),
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    # TODO
    # SETAR A VARIAVEL ABAIXO NAS ENVIROMENTS DO HEROKU 
    url_loginme_create_user = os.environ.get("URL_LOGINME_CREATE_USER", "http://localhost:5001/createUser")

    r = requests.post(url_loginme_create_user, data = json.dumps(jsonProntoParaEnvio), headers = headers)

    if str (r.status_code)[0] != "2":
        print("[X] >> Ocorreu um erro no Log-in-me")
        return r.text, r.status_code

    return r.text, 201

def vinculateApp(userId, appName, secret):
    db = mongo_connection.getDb()

    res = db["users"].insert_one({
        "idLoginme": userId,
        "applications": [{
            "name": appName,
            "secret": secret
        }]
    }) 

    print(">> Aplicação vinculada, o ID gerado foi: ", res.inserted_id)