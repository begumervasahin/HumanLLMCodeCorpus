import sys
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    selection_sort(A)
    print("Sorted array:", end=" ")
    for num in A:
        print(num, end=" ")