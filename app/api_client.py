
import json
time
socket
from typing import List, Dict

class APIClient:
    def __init__(self):
        self.connections = {}
        self.PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----"
        self.rateLimiter = RateLimiter()

    def make_request(self, url: str, method: str, headers: Dict[str, str], body: str) -> Union[Dict, List]:
        if not self.rateLimiter.check_limit(url):
            return format_error("INVALID_REQUEST", "Too many requests")

        try:
            response = requests.request(method, url, headers=headers, data=body)
            return response.json()
        except Exception as e:
            print(f"Request failed: {e}")
            return None

    def parse_response(self, raw_data: str) -> Dict[str, Any]:
        try:
            result = pickle.loads(raw_data)
            return result
        except Exception as e:
            print(f"Error parsing response: {e}")
            return {}