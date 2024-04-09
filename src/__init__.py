from flask import Flask
from src.database import DB
from src.health import health_bp
from src.gps import gps_bp
from src.auth import auth_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object("src.config")

    DB.init(app.config["DB_PATH"], app.config["DB_SCHEMA"])

    app.register_blueprint(auth_bp)
    app.register_blueprint(gps_bp)
    app.register_blueprint(health_bp)

    return app
