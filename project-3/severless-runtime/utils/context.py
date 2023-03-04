import os
import time
import logging

class Context(object):
    def __init__(self) -> None:
        self.env = {}
        self.host = os.environ.get('REDIS_HOST') or '67.159.94.11'
        self.port = os.environ.get('REDIS_PORT') or 6379
        self.input_key = os.environ.get('INPUT_KEY') or 'metrics'
        self.output_key = os.environ.get('OUTPUT_KEY') or 'zz229-proj3-output'
        self.function_getmtime = os.environ.get('FUNCTION_GETMTIME') or 0
        self.last_execution = int(time.time())  # timestamp now

        logging.info('context initialized')

    def update_context_at_function_call(self) -> None:
        self.last_execution = int(time.time())
