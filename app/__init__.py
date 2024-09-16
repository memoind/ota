from flask import Flask
from .routes import bp

def create_app():
    app = Flask(__name__)

    # Registrando o blueprint
    app.register_blueprint(bp)

    return app
