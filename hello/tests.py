import unittest

from pyramid import testing


class HelloViewTests(unittest.TestCase):
    def setup(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from .views import hello_world
        request = testing.DummyRequest()
        string = hello_world(request)
        self.assertEqual(string, 'Hello World')

    def test_hello_world2(self):
        from .views import hello_world2
        request = testing.DummyRequest()
        response = hello_world2(request)
        self.assertEqual(response.status_code, 200)
