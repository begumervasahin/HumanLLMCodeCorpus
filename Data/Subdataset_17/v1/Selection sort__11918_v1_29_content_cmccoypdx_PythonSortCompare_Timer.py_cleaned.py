import timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
def TimeFunc(func, *args, **kwargs):
    wrapped = wrapper(func, *args, **kwargs)
    return timeit.timeit(wrapped, number=1)
if __name__ == "__main__":
    def sample_function(x, y):
        return x + y
    time_taken = TimeFunc(sample_function, 3, 5)
    print(f"Time taken to execute sample_function: {time_taken} seconds")