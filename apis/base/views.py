import flask
import jwt
from flask_cors import CORS
from flask_jwt_extended import exceptions

from apis.base.errors import errors

api = flask.Blueprint('api', __name__, url_prefix='/v1')
CORS(api)


@api.errorhandler(Exception)
def catch_errors(error):
    if isinstance(error, exceptions.NoAuthorizationError):
        error = errors.MissingAuthorizationHeader()
    elif isinstance(error, jwt.exceptions.ExpiredSignatureError):
        error = errors.ExpiredTokenError()
    if not isinstance(error, errors.BadRequestParameter):
        raise error

    return flask.jsonify(
        message=error.msg,
        error=error.msg,
    ), error.error_code
