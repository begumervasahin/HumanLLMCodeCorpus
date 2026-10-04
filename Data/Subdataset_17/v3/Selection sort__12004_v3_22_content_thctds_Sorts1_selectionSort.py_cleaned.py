def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
def get_user_input():
    num_elements = int(input("Enter the number of elements: "))
    arr = []
    print("Enter the elements:")
    for _ in range(num_elements):
        element = int(input("Element: "))
        arr.append(element)
    return arr
def main():
    arr = get_user_input()
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
if __name__ == "__main__":
    main()