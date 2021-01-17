import logging

import flask

from apis.base.views import api
from apis.version import APP_VERSION

logger = logging.getLogger(__name__)


@api.route('/status', methods=['GET'])
def status():
    logger.debug('get status endpoint')

    return flask.jsonify(
        version=APP_VERSION,
    ), 200
