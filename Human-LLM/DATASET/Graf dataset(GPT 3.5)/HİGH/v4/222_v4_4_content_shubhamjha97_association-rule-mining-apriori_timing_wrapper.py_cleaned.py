
from time import time
def fonk1(fn):
    def fonk2(*args, **kwargs):
        b1 = time()
        b2 = fn(*args, **kwargs)
        b3 = time() - b1
        print(f"Function '{fn.__name__}' took {b3:.6f} seconds.")
        return b2
    return wrapper