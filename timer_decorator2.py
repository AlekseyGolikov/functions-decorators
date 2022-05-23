import time
from unittest import result

def timer(func):
    def wrapper():
        start = time.perf_counter()
        result = func()
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime} sec.")
        wrapper.__name__ = func.__name__
        return result
    return wrapper

@timer
def calculation():
    time.sleep(1)
    return f"{calculation.__name__} is completed"

print(calculation())