from flask import Flask
from routes import app_blueprint

def create_app():
    app = Flask("__main__")
    app.register_blueprint(app_blueprint)
    # Reload automático
    app.run(debug=True)
    return app