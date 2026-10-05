import time
from matplotlib import pyplot as plt
test_case = list(range(1000))
execution_times = []
def linear_search(lst, target):
    for num in lst:
        if num == target:
            return True
        if num > target:
            return False
    return False
def test_linear_search(lst):
    for target in lst:
        start_time = time.time()
        found = linear_search(lst, target)
        end_time = time.time()
        if found:
            execution_times.append(end_time - start_time)
    return execution_times
def plot_execution_times(lst, times):
    plt.plot(lst, times, color='green', marker='o', linestyle='solid')
    plt.title("Linear Search Performance")
    plt.xlabel('Test Case')
    plt.ylabel('Execution Time (s)')
    plt.show()
execution_times = test_linear_search(test_case)
plot_execution_times(test_case, execution_times)