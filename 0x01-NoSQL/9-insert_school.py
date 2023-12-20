#!/user/bin/env python3
"""
insert a document in Python
"""

def insert_school(mongo_collection, **kwargs):
    """inserts new document"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
