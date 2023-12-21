#!/usr/bin/env python3
"""
Redis Basics
"""
import redis
import uuid
from typing import Union


class Cache:
    """A cache class for storing redis data"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores `data` in redis storage"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
