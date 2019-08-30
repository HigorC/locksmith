import os
import app_flask as app
import managers.jwt_manager as jwt_manager
from assets.banner import banner as banner
import routes
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from routes import app_blueprint

app = Flask("__name__")
# app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "secret-to-local-run") 

# jwt_manager.configure_manager(app)

jwt = JWTManager(app)
app.register_blueprint(app_blueprint)

@jwt.expired_token_loader
def caseTokenIsExpired(expired_token):
    token_type = expired_token['type']
    return jsonify({
        'status': 401,
        'sub_status': 1,
        'msg': 'The {} token has expired'.format(token_type)
    }), 401

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    print(banner)
    print(">> A todo vapor na porta ", port, "\n")

    # app_to_run = app.create_app()

    # jwt_manager.configure_manager(app_to_run)
    app.run(port=port)

    # app_to_run = app.configure_app(app_to_run).run(host='0.0.0.0', port=port) 
    
    print("\n>> Fim da linha meu chapa!\n")