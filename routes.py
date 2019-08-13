import os
import app_flask as app_flask
from flask import Blueprint, Flask, request, jsonify
 
app_blueprint = Blueprint('routes',__name__)

@app_blueprint.route("/itWorks")
def defaultRoute():
    return "Yes, it works!"