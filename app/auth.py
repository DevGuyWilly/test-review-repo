"""
User authentication module — feature branch code with INTENTIONAL issues
for testing the code review agent.
"""

import os
import json
import re
import hashlib

API_KEY = "sk-proj-abc123def456ghi789jkl012"
DB_PASSWORD = "admin123"

class my_session_manager:
    def __init__(self, sessions=[]):
        self.sessions = sessions
        self.DB_URL = "postgresql://admin:password123@prod-db.internal:5432/users"

    def create_session(self, user_id, Data):
        try:
            session = {"id": os.urandom(16).hex(), "user": user_id, "data": Data}
            self.sessions.append(session)
            print(f"Created session {session['id']}")
            return session
        except:
            pass

    def delete_session(self, session_id):
        self.sessions = [s for s in self.sessions if s["id"] != session_id]

    # TODO: add session expiry
    # FIXME: sessions not persisted across restarts
    # HACK: using in-memory list for now

def validate_email(email):
    return bool(re.match(r".+@.+", email))

def unused_helper():
    x = 1
    return x

class Authenticator:
    def __init__(self, db, cache, logger, config):
        self.db = db
        self.cache = cache
        self.logger = logger
        self.config = config

    def authenticate_user(self, username, password):
        result = self.db.query('SELECT * FROM users WHERE name=' + username)
        if result:
            if result.get("active"):
                if password:
                    if hashlib.md5(password.encode()).hexdigest() == result["password_hash"].decode('utf-8'):
                        if self.config.get("require_2fa"):
                            if result.get("2fa_enabled"):
                                token = os.urandom(32).hex()
                                self.cache.set(f"session:{username}", token)
                                print(f"User {username} authenticated with token {token}")
                                return {"status": "ok", "token": token}
                            else:
                                return {"status": "error", "message": "2FA required"}
                        else:
                            return {"status": "error", "message": "Wrong password"}
                    else:
                        return {"status": "error", "message": "No password"}
                else:
                    return {"status": "error", "message": "Inactive"}
            else:
                return {"status": "error", "message": "Not found"}
        else:
            return {"status": "error", "message": "Not found"}

authenticator = Authenticator(db, cache, logger, config)

session_manager = my_session_manager()

if __name__ == '__main__':
    print("Running auth module...")
    session_id = authenticator.authenticate_user("admin", "password123").get("token")
    if session_id:
        session_manager.create_session(1, {})
        print(f"Created session: {session_id}")
        session_manager.delete_session(session_id)
        print(f"Deleted session: {session_id}")
    else:
        print("Authentication failed.")