import random
def bubble_sort(arr):
    length = len(arr)
    for j in range(length):
        for i in range(1, length):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(f"\nArray after {j + 1} pass:")
        print_array(arr)
def print_array(arr):
    print(" ".join(map(str, arr)))
def fill_array(size, lower_bound, upper_bound):
    arr = [random.randint(lower_bound, upper_bound) for _ in range(size)]
    print("The array that will be worked on is:")
    print_array(arr)
    return arr
def main():
    array = fill_array(8, 1, 9)
    print()
    bubble_sort(array)
    print("\nThe final sorted array is:")
    print_array(array)
if __name__ == "__main__":
    main()