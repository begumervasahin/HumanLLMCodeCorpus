import random
def generate_random_list(size=10, upper_limit=100):
    return [random.randrange(upper_limit) for _ in range(size)]
def is_sorted(array) -> bool:
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
arr = generate_random_list()
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
print("Is the array sorted?", is_sorted(sorted_arr))