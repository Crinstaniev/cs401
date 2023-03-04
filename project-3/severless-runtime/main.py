# Entry-point of the severless runtime. The runtime does the following:
# 1. Create a thread to run regular tasks to fetch psutil data and push to redis metrics.
# 2. Load usermodule
# 3. Run usermodule's handler function.
# 4. Catch the exception and log it to terminal.

import importlib
import logging
import os
import time

from utils.context import Context
from utils.redis_connection import RedisConnection

# set log level
if os.environ.get('LOG_LEVEL') == 'INFO':
    log_level = logging.INFO
else:
    log_level = logging.DEBUG

# logging config
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=log_level)

# iniitialize the context
context = Context()

# initialize the redis connection from input class.
redis_connection = RedisConnection(context.host, context.port)

# load usermodule
try:
    usermodule = importlib.import_module('usermodule')
    logging.info('usermodule loaded')
except:
    usermodule = importlib.import_module('usermodule_dummy')
    logging.error('no usermodule found')

# main loop
while True:
    # fetch metrics
    metrics = redis_connection.fetch_metrics()
    logging.debug(metrics)
    # run usermodule's handler function
    payload = usermodule.handler(metrics, context)
    logging.debug(payload)
    # push the output to redis
    redis_connection.push_output(context.output_key, payload)
    # update context
    context.update_context_at_function_call()
    logging.info('handler function executed')
    # sleep for 1 second
    time.sleep(1)
