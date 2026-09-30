import logging
import random
import time

class TemporaryError(Exception):
    """Stand-in for a timeout / 429 / 503"""

def call_with_retry(func, max_attempts=4):
    for attempt in range(max_attempts):
        try:
            return func()
        except:
            if attempt == max_attempts - 1:
                raise
            wait = 2 ** attempt + random.uniform(0, 1)