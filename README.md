# *Locksmith - The Guardian of Keys*

Administrador de chaves e *Tokens*, responsável por certificar uma comunicação segura entre *API's*.

### Instalação

Instalar as libs utilizadas no projeto:

```
pip install flask
pip install flask-jwt-extended
```

### Para rodar
```
python run.js
```

## Funcionamento

Para proteger a comunicação entre *API's*, alguma autenticação deve ser realizada. Por isso, o *Locksmith* implementa e utiliza *Tokens JWT*.

Para que seja utilizado corretamente, o *Locksmith* deve ser utilizado dos dois lados da comunicação, isto é, necessitando uma *API* A conversar com uma *API* B, ambas devem se relacionar com o *Locksmith*, a fim de estabelecer uma autenticação.

### Exemplo 1 - Utilização de *Token* Válido

O caso de uso perfeito é demonstrado na imagem abaixo.

![Exemplo 1](https://github.com/HigorC/locksmith/blob/master/assets/fluxogramas/token_valido.png)

**1.** A *API* 1 faz uma requisição para o *Locksmith*, lhe pedindo um *Token JWT*.

**2.** O *Locksmith* responde a requisição, gerando e retornando um *Token JWT*.

**3.** A *API* 1 faz uma requisição para a *API* 2, com o *Token* provido setado no *header Authorization*.

**4.** *API* 2 faz uma requisição para o *Locksmith*, lhe pedindo para validar o *Token JWT*.

**5.** Sendo o *Token JWT* válido, o *Locksmith* retorna o objeto armazenado no *identity* do *Token JWT* para a *API* 2.

**6.** A *API* 2 responde a requisição feita no passo (3).

### Exemplo 2 - Utilização de *Token* Inválido

A imagem abaixo demonstra um exemplo em que é utilizado na requisição um Token JWT que não foi criado pelo *Locksmith*.

![Exemplo 2](https://github.com/HigorC/locksmith/blob/master/assets/fluxogramas/token_invalido.png)

**1.** A *API* 1 faz uma requisição para a *API* 2, com um *Token JWT* qualquer.

**2.** *API* 2 faz uma requisição para o *Locksmith*, lhe pedindo para validar o *Token JWT*.

**3.** Sendo o *Token JWT* inválido, o *Locksmith* retorna um erro, informando que a autenticação falhou.

**4.** A *API 2* responde a requisição feita no passo (1), propagando o erro obtido ou tratando-o.

### Exemplo 3 - Não utilização de Token

A imagem abaixo demonstra um exemplo em que é feita uma requisição sem utilizar nenhum Token JWT.

![Exemplo 3](https://github.com/HigorC/locksmith/blob/master/assets/fluxogramas/sem_token.png)

**1.** A *API* 1 faz uma requisição para a *API* 2, sem nenhum *Token*.

**2.** Estando as rotas da *API* 2 configuradas para responderem apenas as requisições com um *Token* setado no *Header*, a *API 2* responde a requisição feita no passo (1) com um erro de autenticação.
