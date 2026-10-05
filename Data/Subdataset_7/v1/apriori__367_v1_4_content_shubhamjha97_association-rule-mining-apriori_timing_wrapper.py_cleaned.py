from time import time
def fonk1(fn):
    def fonk2(*args, **kwargs):
        b1 = time()
        b2 = fn(*args, **kwargs)
        print(fn.b3, "took", time() - b1, "seconds.")
        return b2
    return wrapper
@timeit
def fonk3():
    for i in range(1000000):
        pass
if b3 = = "__main__":
    fonk3()