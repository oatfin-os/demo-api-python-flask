import logging
import uuid

import flask
from flask_jwt_extended import jwt_required

from apis.base.views import api
from apis.tasks import tasks

logger = logging.getLogger(__name__)


@api.route('/tasks', methods=['POST'])
@jwt_required
def task():
    logger.debug('task api')
    task_id = uuid.uuid4()

    tasks.print_value_on_demand.apply_async(task_id=task_id)

    return flask.jsonify(
        task_id=task_id
    ), 200
