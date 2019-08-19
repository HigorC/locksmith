from flask import abort
import re
import utils.exception_messages as exception_messages
import requests

def validateRequest(request):
    email = request.get("email")
    username = str(request.get("username")) if request.get("username") is not None else None
    password = str(request.get("password")) if request.get("password") is not None else None

    if ((email is None or (not email.strip())) or 
        (username is None or (not username.strip()) or len(username) < 4) or
        (password is None or (not password.strip()) or len(password) < 4)):
        print("[X] >> A requisição não contém um ou mais campos obrigatórios!")
        abort(400, exception_messages.getMsgRequisicaoInvalida())

    if isEmailInvalidByRegex(email):
        print("[X] >> O email informado na requisição é inválido!")
        abort(400, "O email informado na requisição é inválido!")

def isEmailInvalidByRegex(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None

def isUserLogged(token):

    headers = {"authorization": token}

    # TODO 
    # Rota no heroku
    
    res = requests.get("http://localhost:5001/isLogged", headers=headers)

    if str (res.status_code)[0] != "2":
        print("[X] >> Ocorreu um erro no Log-in-me")
        abort(res.text, res.status_code)

    return res.json().get("isLogged")
