import time
def calculate_e_number(start, end):
    for i in range(start, end):
        result = (1 + (1 / i)) ** i
        print(result)
def calculate_and_measure_execution_time():
    start_time = time.time()
    calculate_e_number(1, 100000)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
if __name__ == "__main__":
    calculate_and_measure_execution_time()