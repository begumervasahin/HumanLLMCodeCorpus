import random
def generate_random_list(length: int) -> list[int]:
    return [random.randrange(100) for _ in range(length)]
def is_sorted(array: list) -> bool:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True
def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
def main():
    original_array = generate_random_list(10)
    print("Original array:")
    print(original_array)
    sorted_array = insertion_sort(original_array)
    print("Sorted array:")
    print(sorted_array)
    if is_sorted(sorted_array):
        print("Array is sorted.")
    else:
        print("Array is not sorted.")
if __name__ == "__main__":
    main()