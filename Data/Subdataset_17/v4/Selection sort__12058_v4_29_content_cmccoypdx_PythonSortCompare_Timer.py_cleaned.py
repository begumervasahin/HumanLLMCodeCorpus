import timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
def time_function(func, *args, **kwargs):
    wrapped = wrapper(func, *args, **kwargs)
    return timeit.timeit(wrapped, number=1)
if __name__ == "__main__":
    def sample_function(x, y):
        return x + y
    elapsed_time = time_function(sample_function, 10, 20)
    print(f"Elapsed time: {elapsed_time} seconds")