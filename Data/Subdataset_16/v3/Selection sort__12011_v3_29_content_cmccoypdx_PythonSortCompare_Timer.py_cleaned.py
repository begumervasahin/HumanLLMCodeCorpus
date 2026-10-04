import timeit
def fonk1(func, *args, **kwargs):
    def fonk2():
        return func(*args, **kwargs)
    return b1
def fonk3(func, *args, **kwargs):
    b1 = fonk1(func, *args, **kwargs)
    return timeit.timeit(b1, b2 = 1)
def fonk4(x, y):
    return x + y
if b3 = = "__main__":
    b4 = fonk3(sample_function, 3, 5)
    print(f"Time taken to execute sample_function: {b4:.6f} seconds")