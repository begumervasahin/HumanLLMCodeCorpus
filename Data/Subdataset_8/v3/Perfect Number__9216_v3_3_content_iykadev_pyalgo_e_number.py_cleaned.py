import time
import math
def calculate_e_power_integers(start, end):
    for i in range(start, end):
        result = math.exp(i)
        print(result)
def measure_execution_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
def calculate_and_measure_execution_time():
    measure_execution_time(calculate_e_power_integers, 1, 100000)
if __name__ == "__main__":
    calculate_and_measure_execution_time()