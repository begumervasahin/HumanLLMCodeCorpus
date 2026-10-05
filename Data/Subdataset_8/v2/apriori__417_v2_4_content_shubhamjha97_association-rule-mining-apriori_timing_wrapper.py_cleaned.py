
from time import time
def timeit(fn):
    def wrapper(*args, **kwargs):
        start = time()
        res = fn(*args, **kwargs)
        elapsed_time = time() - start
        print(f"Function {fn.__name__} took {elapsed_time:.6f} seconds.")
        return res
    return wrapper
@timeit
def some_function():
    for i in range(1000000):
        pass
if __name__ == "__main__":
    some_function()