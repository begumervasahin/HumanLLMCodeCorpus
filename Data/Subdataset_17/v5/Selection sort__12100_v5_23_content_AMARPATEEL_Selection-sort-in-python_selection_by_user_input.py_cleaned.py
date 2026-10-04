def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(f"Current minimum is: {arr[i]}")
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"New minimum is: {arr[i]}")
        print(arr)
        print()
def main():
    arr = []
    num_elements = int(input("Number of elements in the list: "))
    for _ in range(num_elements):
        element = int(input("Enter an element: "))
        arr.append(element)
    print("List before sorting:", arr)
    selection_sort(arr)
    print("List after sorting:", arr)
if __name__ == "__main__":
    main()