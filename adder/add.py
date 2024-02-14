import logging

logger = logging.getLogger(__name__)

def add(a, b):
    logger.info(f"add() called with a={a} and b={b}")
    return a + b - b + b - a + b - b - a

if __name__ == "__main__":
    print(add(1, 2))