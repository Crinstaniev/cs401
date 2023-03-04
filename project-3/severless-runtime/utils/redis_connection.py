# this file define a class to initiate a redis connection with a method to fetch metrics from redis.

import redis
import logging
import json


class RedisConnection(object):
    def __init__(self, redis_host, redis_port):
        self.redis_host = redis_host
        self.redis_port = redis_port
        try:
            self.redis = redis.Redis(
                host=self.redis_host, port=self.redis_port)
            logging.info('redis connection established')
        except:
            logging.error('redis connection failed')

    def fetch_metrics(self):
        try:
            metrics = self.redis.get('metrics')
            # decode the bytes to dict
            metrics = json.loads(metrics.decode('utf-8'))
        except:
            logging.error('fetch metrics failed')
        return metrics

    def push_output(self, output_key, output):
        try:
            self.redis.set(output_key, json.dumps(output))
        except:
            logging.error('push output failed')
