import timeit
def fonk1(func, *args, **kwargs):
    def fonk2():
        return func(*args, **kwargs)
    return b1
def fonk3(func, *args, **kwargs):
    b1 = fonk1(func, *args, **kwargs)
    return timeit.timeit(b1, b2 = 1)
if b3 = = "__main__":
    def fonk4(x, y):
        return x + y
    b4 = fonk3(sample_function, 10, 20)
    print(f"Elapsed time: {b4} seconds")