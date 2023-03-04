# Entry-point of the severless runtime. The runtime does the following:
# 1. Create a thread to run regular tasks to fetch psutil data and push to redis metrics.
# 2. Load usermodule
# 3. Create a thread to run usermodule's handler function.
# 4. Catch the exception and log it to terminal.

import importlib
import logging
import os

from utils.input import Input

# logging config
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


# load environment variables

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
if REDIS_HOST is None or REDIS_PORT is None:
    REDIS_HOST = '67.159.94.11'
    REDIS_PORT = 6379
    logging.error(
        'no environment variables found. use default values')
else:
    logging.info('environment variables found:', REDIS_HOST, REDIS_PORT)

# initialize the redis connection from input class.
redis_input = Input(REDIS_HOST, REDIS_PORT)

# load usermodule
try:
    usermodule = importlib.import_module('usermodule')
    logging.info('usermodule loaded')
except:
    usermodule = importlib.import_module('usermodule_dummy')
    logging.error('no usermodule found')
