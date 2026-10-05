import random
def bubble_sort(arr):
    length = len(arr)
    for j in range(length):
        for i in range(1, length):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(f"Array after {j} sort is:")
        print_array(arr)
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
    print()
def fill_array(arr, size):
    for _ in range(size):
        arr.append(random.randint(1, 9))
    print("The array that will be worked on is:")
    print_array(arr)
array = []
size = 8
fill_array(array, size)
bubble_sort(array)
print("\nTHE FINAL SORTED ARRAY IS")
print_array(array)