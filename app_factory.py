from flask import Flask
from routes import home_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    return app