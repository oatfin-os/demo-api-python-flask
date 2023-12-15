import logging

import bcrypt
from bson import ObjectId

from apis.settings import app_config
from apis.users import errors
from apis.users.models import User

logger = logging.getLogger(__name__)


class UserService(object):

    def create(self, username, password):
        logger.debug('Creating user with username=%s', username)

        existing_user = self._lookup_username(username)
        if existing_user is not None:
            raise errors.UserExistError()

        user = User(
            username=username,
            password=PasswordService.encrypt_password(password)
        )

        return user.save()

    def authenticate(self, username, password):
        logger.debug('Authenticating user with username=%s', username)

        user = self._lookup_username(username)
        if user is None or \
                not PasswordService.verify_password(
                    password, user.password
                ):
            raise errors.InvalidUserError()

        return user

    def _lookup_username(self, username):
        logger.debug('Fetching user with username=%s', username)

        return User.objects(
            username=username
        ).first()

    def _look_up(self, user_id):
        logger.debug('Fetching user with user_id=%s', user_id)

        user = User.objects(
            id=ObjectId(user_id)
        ).first()

        if user is None:
            raise errors.UserNotFoundError(
                'No user found with user_id={}'.format(user_id)
            )

        return user

    def delete(self, user_id):
        logger.debug('Delete user with user_id=%s', user_id)

        user = self._look_up(user_id)
        user.delete()


class PasswordService(object):
    @staticmethod
    def encrypt_password(password_text):
        logger.debug('calling encrypt_password.')

        return bcrypt.hashpw(
            password_text.encode('utf-8'),
            app_config.HASH_SALT
        )

    @staticmethod
    def verify_password(provided_password, user_password):
        logger.debug('calling verify_password.')

        return bcrypt.checkpw(
            provided_password.encode('utf-8'),
            user_password.encode('utf-8')
        )
