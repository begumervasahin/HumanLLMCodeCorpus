def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        print(f"Current minimum is: {arr[min_index]}")
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"New minimum is: {arr[i]}")
        print(arr)
        print()
def main():
    arr = []
    num_elements = int(input("Number of elements in the list: "))
    for i in range(num_elements):
        element = int(input("Enter an element: "))
        arr.append(element)
    print("List before sorting:", arr)
    selection_sort(arr)
    print("List after sorting:", arr)
if __name__ == "__main__":
    main()