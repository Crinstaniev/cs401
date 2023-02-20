import unittest
from pprint import pprint
import pandas as pd

import requests

CLUSTER_IP = '10.106.208.198'


class TestAPI(unittest.TestCase):
    def test_api(self):
        url = 'http://{}:30510/api/health'.format(CLUSTER_IP)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok'})

    def test_recommend(self):
        url = 'http://{}:30510/api/recommend'.format(CLUSTER_IP)
        songs_list = pd.read_csv(
            '../data/songs.csv')['track_name'].unique().tolist()
        payload = {
            "songs": songs_list
        }
        print('\npalyload: ')
        pprint(payload)
        response = requests.post(url, json=payload)
        print('\nresponse: ')
        pprint(response.json())
        self.assertEqual(response.status_code, 200)
