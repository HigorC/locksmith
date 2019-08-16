import requests
import json
import managers.jwt_manager as jwt_manager
import os
import utils.validator as validator

def createUser(jsonFromRequest = {}):
    validator.validateRequest(jsonFromRequest)

    print(">> Usuário validado!")

    jsonProntoParaEnvio = {
        "user": jsonFromRequest,
        "application": "locksmith"
    }
    
    headers = {
        'Authorization': jwt_manager.createToken(),
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