#!/usr/bin/env python3
"""
expirable web cache and tracker
"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()


def cacher(method: Callable) -> Callable:
    """decorator for caching"""
    @wraps(method)
    def wrapper(url) -> str:
        """caches ouput"""
        redis_store.incr(f"count:{url}")
        cached_result = redis_store.get(f"result:{url}")
        if cached_result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f"count:{url}", 0)
        redis_store.setex(f"result:{url}", 10, result)
        return result

    return wrapper


@cacher
def get_page(url: str) -> str:
    """makes a request to url and caches result"""
    return requests.get(url).text
