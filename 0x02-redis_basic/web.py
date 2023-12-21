#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def cache_data(method):
    """ Decorator counting how many times
    a URL is accessed """
    @wraps(method)
    def wrapper(url):
        cached_data = store.get(f"cached:{url}")
        if cached_data:
            return cached_data.decode("utf-8")

        data = method(f"count:{url}")

        store.incr(count_key)
        store.set(cached_key, data)
        store.expire(cached_key, 10)
        return html
    return wrapper


@cache_data
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    return requests.get(url).text
