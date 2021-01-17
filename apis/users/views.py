import logging

import flask
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

from apis.base.views import api
from apis.users.services import UserService
from apis.users.validations import validate_user

logger = logging.getLogger(__name__)


@api.route('/login', methods=['POST'])
def login():
    req_data = flask.request.get_json()

    username = req_data.get('username')
    password = req_data.get('password')

    validate_user(username, password, for_login=True)

    logger.debug('login user with username={} endpoint'.format(username))
    user = UserService().authenticate(username, password)

    access_token = create_access_token(identity=user.json())
    logger.debug('access token generated for username={}'.format(username))

    return flask.jsonify(
        message='User login with username={}'.format(username),
        access_token=access_token
    ), 200


@api.route('/users', methods=['POST'])
def create_user():
    req_data = flask.request.get_json()

    username = req_data.get('username')
    password = req_data.get('password')
    validate_user(username, password)

    user = UserService().create(username, password)
    logger.debug('created user with username={}'.format(username))

    return flask.jsonify(
        result=user.json(),
        message='User created with username={}'.format(username),
    ), 200


@api.route('/users/<user_id>', methods=['DELETE'])
@jwt_required
def delete_user(user_id):
    UserService().delete(user_id)
    logger.debug('deleted user with user_id={}'.format(user_id))

    return flask.jsonify(
        message='User deleted with user_id={}'.format(user_id),
    ), 200
