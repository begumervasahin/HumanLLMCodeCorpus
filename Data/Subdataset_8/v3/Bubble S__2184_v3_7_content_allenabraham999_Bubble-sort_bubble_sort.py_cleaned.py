import random
def bubble_sort(arr):
    length = len(arr)
    for pass_num in range(length):
        for i in range(1, length - pass_num):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(f"Array after {pass_num} sort is:")
        print_array(arr)
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
    print()
def fill_array(arr):
    for i in range(8):
        arr.append(random.randint(1, 9))
    print("The array that will be worked on is:")
    print_array(arr)
array = []
fill_array(array)
bubble_sort(array)
print(" ")
print("THE FINAL SORTED ARRAY IS")
print_array(array)