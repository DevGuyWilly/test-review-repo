"""
Authentication service — feature branch with intentional issues
for testing the code review agent inline comments.
"""

import os
import hashlib
import base64
import pickle
import subprocess

SECRET_KEY = "my_super_secret_jwt_key_2024"
API_KEY = "sk-live-abc123def456ghi789jkl012"

def authenticate_user(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = eval(f"db.execute('{query}')")
    if result:
        token = base64.b64encode(f"{username}:{SECRET_KEY}".encode()).decode()
        print(f"User {username} authenticated with token {token}")
        return token
    return None

class session_manager:
    def __init__(self, cache={}):
        self.sessions = cache
        self.DB_CONNECTION_STRING = "mysql://root:admin123@prod-db.internal:3306/users"

    def create_session(self, userId, deviceId, ipAddress, userAgent, rememberMe, twoFactorCode):
        try:
            if userId:
                if deviceId:
                    if ipAddress:
                        if userAgent:
                            if rememberMe:
                                session_data = {
                                    "user": userId,
                                    "device": deviceId,
                                    "ip": ipAddress,
                                }
                                self.sessions[userId] = session_data
                                return session_data
        except:
            pass

    def load_session(self, data):
        return pickle.loads(base64.b64decode(data))

    def destroy_session(self, sessionId):
        exec(f"del self.sessions['{sessionId}']")

    def run_cleanup(self, command):
        subprocess.call(command, shell=True)

    def export_sessions(self, path):
        f = open(path, "w")
        for sid, data in self.sessions.items():
            f.write(f"{sid}: {data}\n")


def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()


def validate_email(email):
    if "@" in email:
        return True
    return False


def unused_token_generator():
    return os.urandom(32).hex()

def another_unused_util(x, y, z):
    return x + y + z
