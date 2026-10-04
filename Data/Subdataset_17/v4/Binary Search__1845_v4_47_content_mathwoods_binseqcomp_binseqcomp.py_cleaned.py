from __future__ import print_function
import random
import timeit
import matplotlib.pyplot as plt
def sequential_search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i
    return -1
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right)
        if x > arr[mid]:
            left = mid + 1
        elif x < arr[mid]:
            right = mid - 1
        else:
            return mid
    return -1
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
def run_search_tests():
    print("\n" + '\x1B[1;7m' + "SEQUENTIAL SEARCH VS BINARY SEARCH" + '\x1B[0m')
    search_results = []
    timeit_loops = 10
    powers_of_ten = range(2, 7)
    for i in powers_of_ten:
        n = 10 ** i
        data = tuple(range(0, n))
        print("\n" + '\x1B[4m' + f"ARRAY SIZE = {n} (10^{i})" + '\x1B[0m')
        for trial in range(1, 4):
            random_value = random.randint(0, n - 1)
            print(f"TRIAL {trial}")
            print(f"Random generated value: {random_value}")
            print("Running SEQ SEARCH...", end="")
            seq_search_time = timeit.timeit(wrapper(sequential_search, data, random_value), number=timeit_loops)
            print("DONE!")
            print(f"Total time for {timeit_loops} searches: {seq_search_time} seconds.")
            print("Running BIN SEARCH...", end="")
            bin_search_time = timeit.timeit(wrapper(binary_search, data, random_value), number=timeit_loops)
            print("DONE!")
            print(f"Total time for {timeit_loops} searches: {bin_search_time} seconds.")
            search_results.append({
                'power': i,
                'trial': trial,
                'array_size': n,
                'random_value': random_value,
                'seq_time': seq_search_time,
                'bin_time': bin_search_time
            })
    return search_results
def plot_results(search_results):
    seq_x = [entry['power'] for entry in search_results]
    seq_y = [entry['seq_time'] for entry in search_results]
    bin_x = [entry['power'] for entry in search_results]
    bin_y = [entry['bin_time'] for entry in search_results]
    plt.plot(seq_x, seq_y, 'rD', label='Sequential Search')
    plt.plot(bin_x, bin_y, 'bo', label='Binary Search')
    plt.axis([0, 7, -0.1, max(seq_y) + 0.1])
    plt.xlabel('Size of Array (powers of 10)')
    plt.ylabel('Search Time (seconds)')
    plt.title('Sequential vs. Binary Search Performance')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()
def main():
    search_results = run_search_tests()
    plot_results(search_results)
    print("\n" + '\x1B[1;7m' + "To end program, close graph window." + '\x1B[0m' + "\n")
if __name__ == "__main__":
    main()