def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(f"Current minimum is: {arr[min_index]} at index {min_index}")
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Swapped {arr[min_index]} with {arr[i]}")
        print("Array state:", arr)
        print()
def get_user_input():
    num_elements = int(input("Number of elements in the list: "))
    arr = []
    for _ in range(num_elements):
        element = int(input("Enter an element: "))
        arr.append(element)
    return arr
def main():
    arr = get_user_input()
    print("List before sorting:", arr)
    print()
    selection_sort(arr)
    print("List after sorting:", arr)
if __name__ == "__main__":
    main()