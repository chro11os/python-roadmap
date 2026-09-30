import logging
import random
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TemporaryError(Exception):
    """Stand-in for a timeout / 429 / 503"""

def call_with_retry(func, max_attempts=4):
    for attempt in range(max_attempts):
        try:
            return func()
        except TemporaryError as e:
            if attempt == max_attempts - 1:
                raise
            wait = 2 ** attempt + random.uniform(0, 1)
            logger.warning("Attempt %d failed (%s), retrying in %.1fs", attempt + 1, e, wait)
            time.sleep(wait)

def flaky_api():
    """fails ~70% of the time, like an overloaded API"""
    if random.random() < 0.7:
        raise TemporaryError("503 Service Unavailable")
    return "success!"

if __name__ == "__main__":
    print (call_with_retry(flaky_api))
    