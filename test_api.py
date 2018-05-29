import unittest
from api import UserCollection

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user_1 = UserCollection('daiel.nuwa@gmail.com', '@1234', 1)
        self.user_2 = UserCollection('danielnuwa84@gmail.com', '@43215', 2)

    def test_get(self):
        self.assertEqual(self.user_1.email, 'daiel.nuwa@gmail.com')
        self.assertEqual(self.user_2.email, 'danielnuwa84@gmail.com')

    def test_put(self):
        pass

    def test_post(self):
        pass
        


if __name__ == '__main__':
    unittest.main()
    