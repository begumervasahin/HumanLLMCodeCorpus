import random
def generate_random_list(size: int) -> list[int]:
    return [random.randrange(100) for _ in range(size)]
def check_sorted(array: list[int]) -> bool:
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))
def insertion_sort(array: list[int]) -> list[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
arr = generate_random_list(10)
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)