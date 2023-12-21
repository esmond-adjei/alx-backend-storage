#!/usr/bin/env python3
"""
expirable web cache and tracker
"""
import redis
import requests
from functools import wraps
from typing import Callable


def cacher(method: Callable) -> Callable:
    """decorator for caching"""
    @wraps(method)
    def wrapper(url) -> str:
        """caches output"""
        local_redis_store = redis.Redis()  # Initialize local Redis store
        local_redis_store.incr(f"count:{url}")
        result = local_redis_store.get(f"result:{url}")
        if result:
            return result.decode('utf-8')

        try:
            result = method(url)
            local_redis_store.set(f"count:{url}", 0)
            local_redis_store.setex(f"result:{url}", 10, result)
            return result
        except Exception as e:
            print(f"Error fetching URL {url}: {e}")
            return ""  # or handle the error according to your requirements

    return wrapper


@cacher
def get_page(url: str) -> str:
    """makes a request to url and caches result"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        raise  # Re-raise the exception for the decorator to handle


# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    content = get_page(url)
    print(content)
