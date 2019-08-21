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

def isUsuarioLogado(token):
    headers = {'Authorization': token}

    r = requests.get("http://localhost:5001/isLogged", headers = headers)

    if str (r.status_code)[0] != "2":
        print("[X] >> Ocorreu um erro no Log-in-me")
        return r.text, r.status_code

    return r.json().get("isLogged")

# Salva no banco de dados (pelo Id do usuário) um novo app com seu secret, caso este
# não existir
def vinculateApp(userId, appName, secret):
    db = mongo_connection.getDb()

    userWithApp = db["users"].find_one({"idLoginme": userId,
        "applications": {"$elemMatch": {"name":appName}}})

    if userWithApp is not None:
        print("[X] >> O usuário já possui esta aplicação vinculada.")
        return "O usuário já possui esta aplicação vinculada.", 400

    res = db["users"].find_one_and_update({"idLoginme": userId},
        {"$addToSet": {
            "applications": {
                "name": appName,
                "secret": secret
            }}
        },  upsert=True,)

    text_success = "A aplicação ["+appName+"] foi vinculada ao usuário ["+userId+"]"

    print(">>", text_success)
    return text_success, 201