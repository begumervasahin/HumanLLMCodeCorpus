import random
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array
if __name__ == "__main__":
    array = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted array:", array)
    sorted_array = insertion_sort(array.copy())
    print("Sorted array:", sorted_array)