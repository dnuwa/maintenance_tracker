
from flask_testing import TestCase

from api import app


class BaseTestCase(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass