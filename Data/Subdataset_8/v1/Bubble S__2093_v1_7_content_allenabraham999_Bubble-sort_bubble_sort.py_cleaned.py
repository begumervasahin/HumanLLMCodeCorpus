import random
def bubble_sort(arr):
    length = len(arr)
    for j in range(length):
        for i in range(1, length):
            if arr[i - 1] > arr[i]:
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
        print(f"array after {j} sort is:")
        print_array(arr)
def print_array(arr):
    for i in range(8):
        print(arr[i], end="")
    print()
def fill_array(arr):
    for i in range(8):
        arr.append(random.randint(1, 9))
    print("the array that will be worked on is:")
    for j in range(8):
        print(arr[j], end="")
    print()
array = []
fill_array(array)
bubble_sort(array)
print(" ")
print("THE FINAL SORTED ARRAY IS")
for i in range(8):
    print(array[i], end="")