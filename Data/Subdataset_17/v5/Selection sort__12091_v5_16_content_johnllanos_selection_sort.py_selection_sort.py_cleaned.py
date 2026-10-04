def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Array after swapping index {i} and {min_index}: {arr}")
def main():
    arr = [100, 48, 70, 29, 2, 17]
    selection_sort(arr)
if __name__ == "__main__":
    main()