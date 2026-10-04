import random
import timeit
import matplotlib.pyplot as plt
def seq_search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i
    return -1
def bin_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r)
        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            return m
    return -1
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
def perform_search_experiments():
    print("\nSEQUENTIAL SEARCH VS BINARY SEARCH")
    results = []
    timeit_loops = 10
    for i in range(2, 7):
        array_size = 10 ** i
        arr = tuple(range(array_size))
        print(f"\nARRAY SIZE = {array_size} (10^{i})")
        for trial in range(1, 4):
            random_value = random.randint(0, array_size - 1)
            print(f"TRIAL {trial}")
            print(f"Random generated value: {random_value}")
            print("Running SEQ SEARCH...", end="")
            seq_time = timeit.timeit(wrapper(seq_search, arr, random_value), number=timeit_loops)
            print("DONE!")
            print(f"Total time for {timeit_loops} searches: {seq_time:.6f} seconds.")
            print("Running BIN SEARCH...", end="")
            bin_time = timeit.timeit(wrapper(bin_search, arr, random_value), number=timeit_loops)
            print("DONE!")
            print(f"Total time for {timeit_loops} searches: {bin_time:.6f} seconds.")
            results.append({
                'power': i,
                'trial': trial,
                'array_size': array_size,
                'random_value': random_value,
                'seq_time': seq_time,
                'bin_time': bin_time,
            })
    return results
def plot_results(results):
    powers = [entry['power'] for entry in results]
    seq_times = [entry['seq_time'] for entry in results]
    bin_times = [entry['bin_time'] for entry in results]
    plt.plot(powers, seq_times, 'rD', label='Seq Search')
    plt.plot(powers, bin_times, 'bo', label='Bin Search')
    plt.xlabel('Size of array (powers of 10)')
    plt.ylabel('Search time (sec)')
    plt.title('Sequential vs. Binary Search Performance')
    plt.grid(True)
    plt.legend(loc='upper left', numpoints=1)
    plt.axis([min(powers) - 1, max(powers) + 1, min(min(seq_times), min(bin_times)) - 0.01, max(seq_times) + 0.1])
    plt.show()
def main():
    results = perform_search_experiments()
    print("\nTo end the program, close the graph window.\n")
    plot_results(results)
if __name__ == "__main__":
    main()