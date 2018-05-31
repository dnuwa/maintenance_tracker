import json
import unittest

from tests.base import BaseTestCase

class TestUserService(BaseTestCase):
    #Tests for the Users Service endpoints

    def test_access_all_users(self):
        #Ensuring the routes behave in a correct way correctly.
        response = self.client.get('/api/v1/users')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        #print(data)
        self.assertIn('email', data)
        self.assertIn('password', data)

    def test_user_registers_successfuly(self):
        datax = {'email':'daniel.nuwa@yahoo.com', 'password':'53423', 'id':1}
        response = self.client.post('/api/v1/users',data = json.dumps(datax), content_type='application/json',)
        #print(response)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)        

    def test_return_all_requests(self):
        response = self.client.get('/api/v1/user/request')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        #print(data)
        self.assertIn('item', data)
            
    def test_access_request_by_id(self):
        response = self.client.get('/api/v1/user/request/1')
        data = json.loads(response.data)
        #print(data)
        self.assertEqual(response.status_code, 200)  

if __name__ == '__main__':
    unittest.main()