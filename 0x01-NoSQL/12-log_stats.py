#!/usr/bin/env python3
"""
log stats
"""
from pymongo import MongoClient


def request_logs(collection):
    """print logs"""
    print(f"{collection.count_documents({})")
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    request_logs(collection)
