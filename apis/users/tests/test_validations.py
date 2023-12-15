import unittest

from apis.base.errors.errors import BadRequestParameter
from apis.users.validations import validate_user


class TestApp(unittest.TestCase):

    def test_success(self):
        errors = validate_user(
            'test@gmail.com',
            '123456789kdkdk'
        )
        self.assertIsNone(
            errors
        )

    def test_short_password(self):
        self.assertRaises(
            BadRequestParameter,
            validate_user,
            'test',
            '123',
            False
        )

    def test_none(self):
        self.assertRaises(
            BadRequestParameter,
            validate_user,
            None,
            None
        )
