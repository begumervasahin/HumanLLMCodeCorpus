def selection_sort(arr):
    for i in range(len(arr)):
        smallest_index = i + arr[i:].index(min(arr[i:]))
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr
def main():
    num_elements = int(input("Enter how many elements you want: "))
    arr = []
    print("Enter numbers in array: ")
    for _ in range(num_elements):
        num = int(input("num: "))
        arr.append(num)
    print("ARRAY:", arr)
    sorted_arr = selection_sort(arr)
    print("SORTED ARRAY:", sorted_arr)
if __name__ == "__main__":
    main()