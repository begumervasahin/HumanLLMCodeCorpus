
from time import time
def timeit(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f"Function '{fn.__name__}' took {elapsed_time:.6f} seconds.")
        return result
    return wrapper