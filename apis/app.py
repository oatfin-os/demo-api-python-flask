import logging

from flask import Flask
from flask_jwt_extended import JWTManager
from mongoengine import connect

from apis.base.views import api as base_api
from apis.status.views import api as status_api
from apis.tasks.views import api as tasks_api
from apis.users.views import api as users_api


def create_app(app_config):
    app = Flask(__name__)

    blueprints = [
        base_api,
        status_api,
        tasks_api,
        users_api,
    ]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.DEBUG = app_config.DEBUG
    app.config['JWT_SECRET_KEY'] = app_config.SECRET_KEY

    logging.basicConfig(level=app_config.LOG_LEVEL)
    logging.getLogger('werkzeug').setLevel(logging.INFO)

    connect(db=app_config.DB_NAME, host=app_config.DB_HOST)

    JWTManager(app)

    return app
