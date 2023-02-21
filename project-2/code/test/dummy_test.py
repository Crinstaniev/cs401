import unittest
from pprint import pprint

import requests


class TestDummyBackend(unittest.TestCase):
    def test_dummy(self):
        url = 'http://localhost:5000/api/recommend'
        response = requests.post(url, json={'songList': [1, 2, 3]})
        pprint(response)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
