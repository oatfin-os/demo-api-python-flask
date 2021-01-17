import json
import unittest

from apis.app import create_app
from apis.settings import app_config

app = create_app(app_config)
test_client = app.test_client()


class TestApp(unittest.TestCase):

    def test(self):
        res = test_client.get(
            'v1/status',
            content_type='application/json'
        )

        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)
        self.assertEqual(data['version'], '0.0.1')


if __name__ == '__main__':
    unittest.main()
