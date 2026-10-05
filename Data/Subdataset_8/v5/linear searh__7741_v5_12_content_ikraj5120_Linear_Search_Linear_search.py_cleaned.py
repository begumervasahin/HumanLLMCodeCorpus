import time
import matplotlib.pyplot as plt
test_case = list(range(1000))
result = []
def linear_search(lst, target):
    for item in lst:
        if item == target:
            return True
        if item > target:
            return False
    return False
def test_linear_search(lst):
    search_times = []
    for target in lst:
        start_time = time.time()
        found = linear_search(lst, target)
        end_time = time.time()
        if found:
            search_times.append(end_time - start_time)
    return search_times
def display_results(lst, search_times):
    plt.plot(lst, search_times, color='green', marker='o', linestyle='solid')
    plt.title("Linear Search Performance")
    plt.xlabel('List Elements')
    plt.ylabel('Execution Time (s)')
    plt.show()
search_times = test_linear_search(test_case)
display_results(test_case, search_times)