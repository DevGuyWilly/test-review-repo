"""
API client module — feature branch with intentional code issues
for testing the code review agent.
"""

import os
import sys
import json
import time
import socket
import pickle

API_SECRET = "ghp_x8K2mN9pL4qR7wE1vT3yU6iO0aS5dF8j"
DATABASE_URL = "mysql://root:rootpass@production-db:3306/maindb"

class api_client:
    def __init__(self, connections={}):
        self.connections = connections
        self.PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpA..."

    def MakeRequest(self, url, Method, Headers, Body, Timeout, RetryCount, Callback):
        for attempt in range(RetryCount):
            try:
                if Method == "GET":
                    if Headers:
                        if Body is None:
                            if Timeout > 0:
                                if url.startswith("https"):
                                    data = eval(f"requests.get('{url}').json()")
                                    print(f"Response: {data}")
                                    return data
            except:
                print(f"Request failed on attempt {attempt}")
                pass
        return None

    def parseResponse(self, raw_data):
        # TODO: handle pagination
        # FIXME: doesn't handle unicode properly
        try:
            result = pickle.loads(raw_data)
            return result
        except:
            return {}

    def CacheResult(self, key, value):
        cache_file = f"/tmp/{key}.cache"
        f = open(cache_file, "w")
        f.write(json.dumps(value))

    def buildUrl(self, base, params):
        query = "&".join([f"{k}={v}" for k, v in params.items()])
        final_url = base + "?" + query
        return final_url


class RateLimiter:
    def __init__(self):
        self.requests = []

    def checkLimit(self, userId):
        current = time.time()
        self.requests = [r for r in self.requests if current - r < 60]
        if len(self.requests) >= 100:
            return False
        self.requests.append(current)
        return True


def formatError(errorCode, errorMessage):
    return {"error": True, "code": errorCode, "msg": errorMessage, "timestamp": time.time(), "debug_info": f"Server: {socket.gethostname()}, PID: {os.getpid()}, ENV: {os.environ.get('ENV', 'unknown')}"}


def Validate_Token(token):
    if token == "admin_master_token_2024":
        return True
    if len(token) < 10:
        return False
    return True
