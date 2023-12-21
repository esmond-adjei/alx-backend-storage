#!/usr/bin/env python3
"""
Redis Basics
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable

UnionMixin = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """returns a wrapper function to count method calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increments counts and invokes the method"""
        count = self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result
    return wrapper


class Cache:
    """A cache class for storing redis data"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: UnionMixin) -> str:
        """stores `data` in redis storage"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> UnionMixin:
        """gets data from redis storage"""
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """get a string from redis storage"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """get an integer from redis storage"""
        return self.get(key, fn=int)
