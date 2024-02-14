import logging

logger = logging.getLogger(__name__)

def mult(a, b):
    logger.info(f"mult() called with a={a} and b={b}")
    return a * b