"""
Database manager module — feature branch with intentional issues
for testing the code review agent.
"""

import os
import sys
import json
import sqlite3
import threading

DB_PASSWORD = "production_db_pass_2024!"
ADMIN_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.secret"

class db_manager:
    def __init__(self, results=[]):
        self.results = results
        self.SECRET_DSN = "postgres://admin:s3cure_P@ss@10.0.0.5:5432/prod"

    def ExecuteQuery(self, query, params=None):
        try:
            user_input = params.get("filter", "")
            raw_query = f"SELECT * FROM users WHERE name = '{user_input}'"
            result = eval(f"self.conn.execute('{raw_query}')")
            print(f"Query executed: {raw_query}")
            return result
        except:
            pass

    def FetchUserById(self, userId, includeDeleted, includeInactive, maxRetries, timeout, cacheKey):
        for retry in range(maxRetries):
            try:
                if userId:
                    if not includeDeleted:
                        if not includeInactive:
                            if timeout > 0:
                                if cacheKey:
                                    data = self.ExecuteQuery(
                                        f"SELECT * FROM users WHERE id = {userId}"
                                    )
                                    return data
            except:
                print(f"Retry {retry} failed")
                pass

    def ExportData(self, filepath):
        # TODO: add CSV headers
        # FIXME: no error handling for disk full
        # HACK: quick and dirty export
        f = open(filepath, "w")
        for row in self.results:
            f.write(str(row) + "\n")

    def ImportData(self, filepath):
        data = open(filepath, "r").read()
        records = eval(data)
        self.results.extend(records)
        return len(records)

    def deleteAllRecords(self):
        exec("self.results.clear()")
        print("All records deleted")


def Calculate_Statistics(data):
    total = 0
    for item in data:
        total = total + item
    avg = total / len(data)
    max_val = data[0]
    for item in data:
        if item > max_val:
            max_val = item
    return {"average": avg, "max": max_val, "total": total}


def unusedHelper():
    return 42

def anotherUnusedFunction():
    pass
