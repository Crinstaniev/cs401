import time
import requests
import json
import subprocess
import os


command = "kubectl get service project2-service-zz229 -n zz229 -o jsonpath='{.spec.clusterIP}'"
output = subprocess.check_output(command, shell=True)

TEST_DURATION = 60
CLUSTER_IP = output.decode("utf-8").strip()
API_URL = "http://{}:30510/api/health".format(CLUSTER_IP)
TIMESTAMP = time.strftime('%Y-%m-%d_%H-%M-%S')
LOG_NAME = "api_status_{}.json".format(TIMESTAMP)
LOG_FOLDER_PATH = "logs"

# create folder if not exist
if not os.path.exists(LOG_FOLDER_PATH):
    os.makedirs(LOG_FOLDER_PATH)


LOG_FILE_PATH = os.path.abspath(LOG_FOLDER_PATH) + "/" + LOG_NAME

# print cluster ip

# create log file
with open(LOG_FILE_PATH, "w") as f:
    f.write("")

print("Testing API status for {} seconds".format(TEST_DURATION))


def test_api_status():
    print("Cluster IP: {}".format(CLUSTER_IP))

    start_time = time.time()

    while time.time() - start_time < TEST_DURATION:
        response = requests.get(API_URL)

        try:
            json_data = response.json()
        except ValueError:
            json_data = {
                "status": "offline",
                "version": "unknown",
                "model_date": "unknown",
                "time": time.strftime('%Y-%m-%d %H:%M:%S')
            }

        # logging test status with time, response and how many seconds left
        print(time.strftime('%Y-%m-%d %H:%M:%S'), json_data,
              "Time left: {}".format(int(TEST_DURATION - (time.time() - start_time))))

        with open(LOG_FILE_PATH, "a") as f:
            f.write(json.dumps(json_data) + "\n")

        time.sleep(1)
