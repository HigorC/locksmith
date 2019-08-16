from flask import abort
import re
import utils.exception_messages as exception_messages

def validateRequest(request):
    email = request.get("email")
    username = str(request.get("username"))
    password =  str(request.get("password"))

    if ((username == None or not username.strip() or len(username) < 4) or
        (password == None or not password.strip() or len(password) < 4)):
        print("[X] >> A requisição não contém um ou mais campos obrigatórios!")
        abort(400, exception_messages.getMsgRequisicaoInvalida())

    if isEmailInvalidByRegex(email):
        print("[X] >> O email informado na requisição é inválido!")
        abort(400, "O email informado na requisição é inválido!")

def isEmailInvalidByRegex(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == None