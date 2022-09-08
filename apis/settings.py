import logging
import os

import bcrypt


class Common(object):
    SECRET_KEY = 'some-secret-key'
    JWT_EXPIRATION_DELTA = 3600
    HASH_SALT = bcrypt.gensalt()
    DB_HOST = 'mongodb://root:abc123@db:27017/?authSource=admin'
    DB_NAME = 'admin'


class Test(Common):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class Dev(Common):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class Prod(Common):
    DEBUG = False
    LOG_LEVEL = logging.INFO


class Environment(object):
    TEST = 'tst'
    DEV = 'dev'
    PROD = 'prd'


def load():
    env = os.getenv('FLASK_ENVIRONMENT')
    settings = Dev
    if env is not None:
        if env.lower() == Environment.TEST:
            settings = Test
        elif env.lower() == Environment.PROD:
            settings = Prod

    return AppSettings(env, settings())


class AppSettings(object):
    def __init__(self, env, settings):
        self.env = env
        self.settings = settings


app_config = load().settings
