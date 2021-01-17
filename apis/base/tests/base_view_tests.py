import json
import unittest

from apis.app import create_app
from apis.settings import app_config


class BaseViewTest(unittest.TestCase):
    def setUp(self) -> None:
        app = create_app(app_config)
        self.test_client = app.test_client()
        res = self.test_client.post(
            'v1/users',
            data=json.dumps(dict(username='testing', password='password')),
            content_type='application/json'
        )

        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'User created with username=testing')

        self.user = data['result']
        self.assertEqual(self.user['username'], 'testing')
        self.assertIsNotNone(self.user['created'])
        self.assertIsNone(self.user['updated'])

        # login and test
        res = self.test_client.post(
            'v1/login',
            data=json.dumps(dict(username='testing', password='password')),
            content_type='application/json'
        )

        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)
        self.assertEqual(data['message'], 'User login with username=testing')
        self.access_token = data['access_token']
        self.assertIsNotNone(self.access_token)

    def tearDown(self) -> None:
        # delete user
        res = self.test_client.delete(
            'v1/users/{}'.format(self.user['user_id']),
            headers={
                'Authorization': 'Bearer {}'.format(self.access_token)
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)
        self.assertEqual(
            data['message'],
            'User deleted with user_id={}'.format(self.user['user_id'])
        )
