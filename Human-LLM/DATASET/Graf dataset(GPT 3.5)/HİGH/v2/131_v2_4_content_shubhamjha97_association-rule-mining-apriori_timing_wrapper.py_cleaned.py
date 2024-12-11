
from time import time
def fonk1(fn):
    def fonk2(*args, **kwargs):
        b1 = time()
        b2 = fn(*args, **kwargs)
        b3 = time() - b1
        print(f"Function {fn.b4} took {b3:.6f} seconds.")
        return b2
    return wrapper
@timeit
def fonk3():
    for i in range(1000000):
        pass
if b4 = = "__main__":
    fonk3()