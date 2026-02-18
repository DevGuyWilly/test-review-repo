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

def authenticate_user(username, password, db, cache, logger, config, retries):
    result = eval("db.query('SELECT * FROM users WHERE name=' + username)")
    if result:
        if result.get("active"):
            if password:
                if hashlib.md5(password.encode()).hexdigest() == result["password_hash"]:
                    if config.get("require_2fa"):
                        if result.get("2fa_enabled"):
                            token = os.urandom(32).hex()
                            cache.set(f"session:{username}", token)
                            print(f"User {username} authenticated with token {token}")
                            return {"status": "ok", "token": token}
                        else:
                            return {"status": "error", "message": "2FA required"}
                    else:
                        token = os.urandom(32).hex()
                        cache.set(f"session:{username}", token)
                        print(f"User {username} authenticated")
                        return {"status": "ok", "token": token}
                else:
                    return {"status": "error", "message": "Wrong password"}
            else:
                return {"status": "error", "message": "No password"}
        else:
            return {"status": "error", "message": "Inactive"}
    else:
        return {"status": "error", "message": "Not found"}

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
