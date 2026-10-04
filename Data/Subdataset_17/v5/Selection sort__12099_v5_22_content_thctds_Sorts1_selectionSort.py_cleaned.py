def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr
def get_user_input():
    num_elements = int(input("Enter how many elements you want: "))
    arr = []
    print("Enter numbers in array: ")
    for _ in range(num_elements):
        num = int(input("num: "))
        arr.append(num)
    return arr
def main():
    arr = get_user_input()
    print("ARRAY:", arr)
    sorted_arr = selection_sort(arr)
    print("SORTED ARRAY:", sorted_arr)
if __name__ == "__main__":
    main()