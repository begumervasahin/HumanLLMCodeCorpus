import random
import time
def binary_search(collection, target):
    low, high = 0, len(collection) - 1
    while high >= low:
        mid = (high + low)
        if target == collection[mid]:
            return mid
        elif target < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def trinary_search(collection, target):
    low, high = 0, len(collection) - 1
    while high >= low:
        one_third = low + (high - low)
        two_thirds = low + 2 * (high - low)
        if target == collection[one_third]:
            return one_third
        elif target < collection[one_third]:
            high = one_third - 1
        elif target == collection[two_thirds]:
            return two_thirds
        elif target < collection[two_thirds]:
            low, high = one_third + 1, two_thirds - 1
        else:
            low = two_thirds + 1
    return -1
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        max_pos = max(range(i + 1), key=lambda x: lst[x])
        lst[i], lst[max_pos] = lst[max_pos], lst[i]
def create_even_list(n):
    lst = random.sample(range(2, 32002, 2), n)
    return lst
def create_odd_list(n):
    lst = random.sample(range(1, 1000000, 2), n)
    return lst
def expand_list(lst):
    return [item for item in lst for _ in range(10)]
def measure_search_time(lst1, lst2):
    start_time = time.time()
    for item in lst2:
        binary_search(lst1, item)
    print(f"Binary Search time: {time.time() - start_time:.6f} seconds")
    start_time = time.time()
    for item in lst2:
        trinary_search(lst1, item)
    print(f"Trinary Search time: {time.time() - start_time:.6f} seconds")
    print()
def run_experiment(n):
    print(f"Experiment with n = {n}")
    print("\nEven integer list:")
    lst1 = create_even_list(n)
    selection_sort(lst1)
    lst2 = expand_list(lst1)
    measure_search_time(lst1, lst2)
    print("Odd integer list:")
    lst2 = create_odd_list(n)
    measure_search_time(lst1, lst2)
def main():
    n_values = [1000, 2000, 4000, 8000, 16000]
    for n in n_values:
        run_experiment(n)
if __name__ == "__main__":
    main()