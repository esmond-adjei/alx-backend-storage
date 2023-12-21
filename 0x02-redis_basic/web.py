#!/usr/bin/env python3
"""expirable cache and tracker"""

import redis
import requests
from typing import Callable
from functools import wraps

redis = redis.Redis()


def cache_data(fn: Callable) -> Callable:
    """cache wrapper"""

    @wraps(fn)
    def wrapper(url):
        """cache and get data"""
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@cache_data
def get_page(url: str) -> str:
    """get page self descriptive
    """
    return = requests.get(url).text
