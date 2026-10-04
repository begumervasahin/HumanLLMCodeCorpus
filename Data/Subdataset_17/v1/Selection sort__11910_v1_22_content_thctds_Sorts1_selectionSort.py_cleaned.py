def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
def main():
    arr = []
    num = int(input("Enter how many elements you want: "))
    print('Enter numbers in array: ')
    for i in range(num):
        n = int(input("num: "))
        arr.append(n)
    print('ARRAY:', arr)
    sorted_arr = selection_sort(arr)
    print('SORTED ARRAY:', sorted_arr)
if __name__ == "__main__":
    main()