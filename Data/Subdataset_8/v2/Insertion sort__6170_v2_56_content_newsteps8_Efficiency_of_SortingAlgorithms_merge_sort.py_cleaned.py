import time
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def print_list(arr):
    for num in arr:
        print(num, end=" ")
    print()
if __name__ == '__main__':
    start_time = time.time()
    count = 0
    with open("case", "r") as fp:
        arr = fp.read().split()
        list2 = [int(x) for x in arr]
    merge_sort(list2)
    print("Sorted array:")
    print_list(list2)
    print("Total comparisons:", count)
    end_time = time.time()
    print("Execution time:", end_time - start_time)