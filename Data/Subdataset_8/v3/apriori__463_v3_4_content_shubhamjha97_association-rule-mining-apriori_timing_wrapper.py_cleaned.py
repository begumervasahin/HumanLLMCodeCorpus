from time import time
def measure_execution_time(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f"Function '{fn.__name__}' took {elapsed_time:.6f} seconds.")
        return result
    return wrapper
@measure_execution_time
def perform_some_processing():
    for _ in range(1000000):
        pass
if __name__ == "__main__":
    perform_some_processing()