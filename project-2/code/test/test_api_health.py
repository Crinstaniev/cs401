import time
import requests
import json
import subprocess
import os


command = "kubectl get service project2-service-zz229 -n zz229 -o jsonpath='{.spec.clusterIP}'"
output = subprocess.check_output(command, shell=True)

TEST_DURATION = 600
CLUSTER_IP = output.decode("utf-8").strip()
API_URL = "http://{}:30510/api/health".format(CLUSTER_IP)
TIMESTAMP = time.strftime('%Y-%m-%d_%H-%M-%S')
LOG_NAME = "api_status_{}.json".format(TIMESTAMP)
LOG_FOLDER_PATH = "logs"

# create folder if not exist
if not os.path.exists(LOG_FOLDER_PATH):
    os.makedirs(LOG_FOLDER_PATH)


LOG_FILE_PATH = os.path.abspath(LOG_FOLDER_PATH) + "/" + LOG_NAME

# create log file
with open(LOG_FILE_PATH, "w") as f:
    f.write("")

print("Testing API status for {} seconds".format(TEST_DURATION))


def test_api_status():
    print("Cluster IP: {}".format(CLUSTER_IP))

    start_time = time.time()

    while time.time() - start_time < TEST_DURATION:
        try:
            response = requests.get(API_URL, timeout=1)
            json_data = response.json()
        except:
            json_data = {
                "status": "offline",
                "version": "unknown",
                "model_date": "unknown",
                "time": time.strftime('%Y-%m-%d %H:%M:%S')
            }

        status = json_data.get("status", "unknown")

        if status == "online":
            # green logs
            print(f"[{int(time.time() - start_time + 1)}/{TEST_DURATION}]",
                  "\033[92m{}\033[0m".format(json.dumps(json_data)))
        else:
            # red logs
            print(f"[{int(time.time() - start_time)}/{TEST_DURATION}]",
                  "\033[91m{}\033[0m".format(json.dumps(json_data)))

        with open(LOG_FILE_PATH, "a") as f:
            f.write(json.dumps(json_data) + "\n")

        time.sleep(1)
