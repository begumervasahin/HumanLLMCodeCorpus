def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)
    left_half = arr[:mid]
    right_half = arr[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(arr, left_half, right_half)
def merge(arr, left, right):
    i = j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
def main():
    num_elements = int(input("How many elements do you want in the list? "))
    arr = [int(input(f"Enter element {i + 1}: ")) for i in range(num_elements)]
    merge_sort(arr)
    print("Sorted list is:", arr)
if __name__ == "__main__":
    main()