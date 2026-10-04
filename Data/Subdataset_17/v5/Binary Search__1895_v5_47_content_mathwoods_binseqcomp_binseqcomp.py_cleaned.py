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
def time_search(func, data, target, loops=10):
    wrapped_func = lambda: func(data, target)
    return timeit.timeit(wrapped_func, number=loops)
def run_search_tests():
    print("\n" + "SEQUENTIAL SEARCH VS BINARY SEARCH")
    search_results = []
    loops = 10
    powers_of_ten = range(2, 7)
    for i in powers_of_ten:
        n = 10 ** i
        data = list(range(n))
        print(f"\nARRAY SIZE = {n} (10^{i})")
        for trial in range(1, 4):
            random_value = random.randint(0, n - 1)
            print(f"TRIAL {trial}")
            print(f"Random generated value: {random_value}")
            print("Running SEQUENTIAL SEARCH...", end="")
            seq_time = time_search(sequential_search, data, random_value, loops)
            print(f"DONE! Total time: {seq_time:.6f} seconds.")
            print("Running BINARY SEARCH...", end="")
            bin_time = time_search(binary_search, data, random_value, loops)
            print(f"DONE! Total time: {bin_time:.6f} seconds.")
            search_results.append({
                'power': i,
                'trial': trial,
                'array_size': n,
                'random_value': random_value,
                'seq_time': seq_time,
                'bin_time': bin_time
            })
    return search_results
def plot_results(search_results):
    seq_times = [entry['seq_time'] for entry in search_results]
    bin_times = [entry['bin_time'] for entry in search_results]
    powers = [entry['power'] for entry in search_results]
    plt.plot(powers, seq_times, 'rD-', label='Sequential Search')
    plt.plot(powers, bin_times, 'bo-', label='Binary Search')
    plt.xlabel('Size of Array (powers of 10)')
    plt.ylabel('Search Time (seconds)')
    plt.title('Sequential vs. Binary Search Performance')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()
def main():
    search_results = run_search_tests()
    plot_results(search_results)
    print("\nTo end the program, close the graph window.\n")
if __name__ == "__main__":
    main()