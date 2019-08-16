def getMsgRequisicaoInvalida():
    return """
     Para criar um usuário, o objeto passado na requisição deve seguir a seguinte estrutura:
     {
         "email": "exemplo@exemplo.com",
         "username": "exemplo",
         "password": 1234
     }

    > O atributo email deve ser um email válido.
    > Os atributos username e password devem possuir ao menos 4 caracteres.
    """