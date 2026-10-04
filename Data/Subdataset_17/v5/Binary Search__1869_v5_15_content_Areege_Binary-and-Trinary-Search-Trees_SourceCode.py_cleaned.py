import random
import time
def binary_search(collection, target):
    low, high = 0, len(collection) - 1
    while low <= high:
        mid = (low + high)
        if collection[mid] == target:
            return mid
        elif collection[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def trinary_search(collection, target):
    low, high = 0, len(collection) - 1
    while low <= high:
        one_third = low + (high - low)
        two_thirds = low + 2 * (high - low)
        if collection[one_third] == target:
            return one_third
        elif collection[two_thirds] == target:
            return two_thirds
        elif target < collection[one_third]:
            high = one_third - 1
        elif target < collection[two_thirds]:
            low, high = one_third + 1, two_thirds - 1
        else:
            low = two_thirds + 1
    return -1
def selection_sort(a_list):
    for fill in range(len(a_list) - 1, 0, -1):
        max_position = 0
        for index in range(1, fill + 1):
            if a_list[index] > a_list[max_position]:
                max_position = index
        a_list[fill], a_list[max_position] = a_list[max_position], a_list[fill]
def create_even_list(n):
    return [x if x % 2 == 0 else x + 1 for x in random.sample(range(1, 16001), n)]
def create_odd_list(n):
    return [x if x % 2 != 0 else x + 1 for x in random.sample(range(1, 1000000), 10 * n)]
def create_duplicate_list(source_list):
    return [item for item in source_list for _ in range(10)]
def check_search_times(sorted_list, search_list):
    start_time = time.process_time()
    for item in search_list:
        binary_search(sorted_list, item)
    print(f"Binary Search time: {time.process_time() - start_time:.5f} seconds")
    start_time = time.process_time()
    for item in search_list:
        trinary_search(sorted_list, item)
    print(f"Trinary Search time: {time.process_time() - start_time:.5f} seconds\n")
def run_experiment(n):
    print(f"Running experiment with n = {n}\n")
    even_list = create_even_list(n)
    selection_sort(even_list)
    duplicate_list = create_duplicate_list(even_list)
    check_search_times(even_list, duplicate_list)
    print(f"Running experiment with odd list of size {10 * n}\n")
    odd_list = create_odd_list(n)
    check_search_times(even_list, odd_list)
def main():
    n_values = [1000, 2000, 4000, 8000, 16000]
    for n in n_values:
        run_experiment(n)
if __name__ == "__main__":
    main()