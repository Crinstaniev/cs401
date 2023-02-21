import unittest
from pprint import pprint

import pandas as pd
import requests
import os
import subprocess


class TestAPI(unittest.TestCase):
    def test_api(self):
        command = "kubectl get service project2-service-zz229 -n zz229 -o jsonpath='{.spec.clusterIP}'"
        output = subprocess.check_output(command, shell=True)
        CLUSTER_IP = output.decode("utf-8").strip()
        url = 'http://{}:30510/api/health'.format(CLUSTER_IP)
        response = requests.get(url, timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok'})

    def test_recommend(self):
        command = "kubectl get service project2-service-zz229 -n zz229 -o jsonpath='{.spec.clusterIP}'"
        output = subprocess.check_output(command, shell=True)
        CLUSTER_IP = output.decode("utf-8").strip()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        url = 'http://{}:30510/api/recommend'.format(CLUSTER_IP)
        songs_list = pd.read_csv(
            '../../data/songs.csv')['track_name'].unique().tolist()
        payload = {
            "songs": songs_list
        }
        response = requests.post(url, json=payload, timeout=5)
        print('\nresponse: ')
        pprint(response.json())
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
