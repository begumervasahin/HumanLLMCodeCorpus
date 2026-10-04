def sort_array(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
def main():
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    sorted_arr = sort_array(arr)
    print("Sorted array:")
    print(sorted_arr)
if __name__ == "__main__":
    main()