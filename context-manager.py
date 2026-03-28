from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Took {end - start} seconds")



def slow_function():
    time.sleep(5)  

with timer():
    slow_function()
