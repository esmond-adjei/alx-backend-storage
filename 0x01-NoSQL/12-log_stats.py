#!/usr/bin/env python3
"""
log stats
"""
from pymongo import MongoClient


client = MongoClient()
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})
print(f"{total_logs} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"    method {method}: {count}")

status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
print(f"{status_check_count} status check")

client.close()
