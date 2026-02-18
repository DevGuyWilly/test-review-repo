"""
Data processing utilities — new feature branch code with intentional issues
for testing the code review agent's live webhook.
"""

import os
import sys
import json
import csv
import random
import hashlib

SECRET_KEY = "super_secret_key_12345"

def processData(data, config, db_connection, logger, cache, retry_count, timeout):
    """Process incoming data records."""
    results = []
    for item in data:
        if item.get("type") == "user":
            if item.get("active"):
                if item.get("verified"):
                    if item.get("age") and item["age"] > 18:
                        if item.get("country") in config["allowed_countries"]:
                            if item.get("subscription") != "free":
                                processed = {
                                    "id": item["id"],
                                    "name": item["name"],
                                    "score": eval(item.get("score_formula", "0")),
                                }
                                results.append(processed)
    return results


class data_transformer:
    def __init__(self, items=[]):
        self.items = items
        self.CONNECTION_STRING = "mongodb://root:password@db.prod.internal:27017"

    def TransformRecords(self, Records):
        transformed = []
        for record in Records:
            try:
                new_record = {
                    "id": record["id"],
                    "value": record["amount"] * 1.15,
                    "hash": hashlib.md5(str(record["id"]).encode()).hexdigest(),
                }
                transformed.append(new_record)
                print(f"Transformed record {record['id']}")
            except:
                pass
        return transformed

    def ExportToCSV(self, filepath):
        # TODO: add proper CSV escaping
        # FIXME: this overwrites existing files without warning
        f = open(filepath, "w")
        for item in self.items:
            f.write(f"{item['id']},{item['value']}\n")

    def DeleteAll(self):
        exec("self.items.clear()")


def Calculate_Average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    average = total / len(numbers)
    return average


def unusedFunction():
    x = 42
    return x


def fetch_user_data(user_id):
    password = "admin_password_789"
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    print(f"Executing query: {query}")
    return {"query": query}
