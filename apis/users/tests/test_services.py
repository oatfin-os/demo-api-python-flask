from apis.base.tests.base_service_tests import BaseServiceTest
from apis.users import errors
from apis.users.services import UserService, PasswordService


class Test(BaseServiceTest):
    def test_lookup(self):
        user = UserService()._look_up(self.user['id'])

        self.assertIsNotNone(user)
        self.assertEqual(
            user['username'],
            'test'
        )

    def test_lookup_username(self):
        user = UserService()._lookup_username(self.user['username'])

        self.assertIsNotNone(user)
        self.assertEqual(
            user['username'],
            'test'
        )

    def test_lookup_username_fail(self):
        user = UserService()._lookup_username('no_user_name')
        self.assertIsNone(user)

    def test_login(self):
        auth = UserService().authenticate('test', 'password')
        self.assertIsNotNone(auth)

    def test_create_fail(self):
        self.assertRaises(
            errors.UserExistError,
            UserService().create, 'test', 'password'
        )

    def test_login_fail(self):
        self.assertRaises(
            errors.InvalidUserError,
            UserService().authenticate, 'test', 'password123456'
        )

    def test_lookup_fail(self):
        self.assertRaises(
            errors.UserNotFoundError,
            UserService()._look_up, '5f17181d1d68a78c0ba04023'
        )

    def test_delete_fail(self):
        self.assertRaises(
            errors.UserNotFoundError,
            UserService().delete, '5f17181d1d68a78c0ba04023'
        )

    def test_encrypt_verify_pass(self):
        hashed = PasswordService.encrypt_password('testing_password_encryption')
        self.assertIsNotNone(hashed)

        match = PasswordService.verify_password(
            'testing_password_encryption',
            '$2b$12$okP67m4XVfIydCankmrULO.ijfaY4LXSnPpXsZxkSu2dc8cdj441C'
        )
        self.assertTrue(match)

    def test_encrypt_verify_fail(self):
        hashed = PasswordService.encrypt_password('testing_password')
        self.assertIsNotNone(hashed)

        match = PasswordService.verify_password(
            'testing_password',
            '$2b$12$okP67m4XVfIydCankmrULO.ijfaY4LXSnPpXsZxkSu2dc558j441C'
        )
        self.assertFalse(match)
