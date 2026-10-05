import random
import time
def binary_search(collection, target):
    low = 0
    high = len(collection) - 1
    while high >= low:
        mid = (high + low)
        if target == collection[mid]:
            return mid
        if target < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def trinary_search(collection, target):
    low = 0
    high = len(collection) - 1
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
            low = one_third + 1
            high = two_thirds - 1
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
def create_list_even(n):
    return random.sample(range(2, 16001, 2), n)
def create_list_odd(n):
    return random.sample(range(1, 1000000, 2), 10 * n)
def create_list2(list1):
    return [num for num in list1 for _ in range(10)]
def check_time(list1, list2):
    t0 = time.clock()
    for index in list2:
        result1 = binary_search(list1, index)
    print("Binary Search time:", time.clock() - t0)
    t0 = time.clock()
    for index in list2:
        result2 = trinary_search(list1, index)
    print("Trinary Search time:", time.clock() - t0, "\n")
def testing(n):
    print("Experiment for n =", n)
    list1 = create_list_even(n)
    selection_sort(list1)
    list2 = create_list2(list1)
    check_time(list1, list2)
    print("Experiment for Odd Numbers")
    list2 = create_list_odd(n)
    check_time(list1, list2)
def main():
    n_values = [1000, 2000, 4000, 8000, 16000]
    for n in n_values:
        print("\nFor n =", n, "\n")
        testing(n)
if __name__ == "__main__":
    main()