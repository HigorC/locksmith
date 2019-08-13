# *Locksmith - The Guardian of Keys*

Administrador de chaves para estabelecer uma comunicação segura entre *API's*.

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

O caso de uso perfeito é demonstrado na imagem abaixo.

![Exemplo 1](https://github.com/HigorC/locksmith/blob/master/assets/fluxogramas/token_valido.png)

**1.** A *API* 1 faz uma requisição para o *Locksmith*, lhe pedindo um *Token JWT*.

**2.** O *Locksmith* responde a requisição, gerando e retornando um *Token JWT*.

**3.** A *API* 1 faz uma requisição para a *API* 2, com o *Token* provido setado no *header Authorization*.

**4.** *API* 2 faz uma requisição para o *Locksmith*, lhe pedindo para validar o *Token JWT*.

**5.** Sendo o *Token JWT* válido, o *Locksmith* retorna o objeto armazenado no *identity* do *Token JWT* para a *API* 2.

**6.** A *API* 2 responde a requisição feita no passo (3).
