import json
import unittest

from tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    #Tests for the Users Service endpoints

    def test_users(self):
        #Ensuring the routes behave in a correct way correctly.
        response = self.client.get('/api/v1/users')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        print(data)
        self.assertIn('email', data)
        self.assertIn('password', data)

    def test_requests(self):
        response = self.client.get('/api/v1/user/request')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        print(data)
        self.assertIn('item', data)




if __name__ == '__main__':
    unittest.main()