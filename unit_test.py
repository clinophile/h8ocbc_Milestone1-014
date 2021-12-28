import unittest
from app import connex_app
import json



BASE_DIRECTORS_URL = '/api/directors'
GET_DIRECTORS_ONE = '{}/7110'.format(BASE_DIRECTORS_URL)


BASE_MOVIES_URL = '{}/movies'.format(GET_DIRECTORS_ONE)
GET_MOVIES_ONE = '{}/48399'.format(BASE_MOVIES_URL)

class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.connex_app = connex_app.app.test_client()
        self.connex_app.testing = True

    
    def test_get_directors(self):
        response = self.connex_app.get(BASE_DIRECTORS_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(data), list)
        
    def test_get_directors_one(self):
        response = self.connex_app.get(GET_DIRECTORS_ONE)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Brian Herzlinger')
        self.assertEqual(type(data), dict)

    def test_get_movies_one(self):
        response = self.connex_app.get(GET_MOVIES_ONE)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['original_title'], 'My Date with Drew')
        self.assertEqual(type(data), dict)


if __name__ == '__main__':
    unittest.main()