import unittest

from apis.users.services import UserService


class BaseServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        created = UserService().create('test', 'password')
        self.assertIsNotNone(created)
        self.user = created

    def tearDown(self) -> None:
        UserService().delete(self.user['id'])
        deleted = UserService()._lookup_username(self.user['username'])
        self.assertIsNone(deleted)
