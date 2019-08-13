from flask import Flask
from routes import app_blueprint

def create_app():
    return Flask("__main__")

def configure_app(app):
    app.register_blueprint(app_blueprint)
    return app