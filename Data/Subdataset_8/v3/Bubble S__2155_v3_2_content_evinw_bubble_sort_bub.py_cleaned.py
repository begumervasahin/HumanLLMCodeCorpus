def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def main():
    unsorted_list = [100, 2993, 22, 1, 82, 11, 33]
    bubble_sort(unsorted_list)
    print("Sorted:")
    for num in unsorted_list:
        print(num, end=" ")
if __name__ == "__main__":
    main()