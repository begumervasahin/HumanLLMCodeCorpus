import random
def insertion_sort(arr):
    for index in range(1, len(arr)):
        current = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current:
            print(f"Swapped {arr[position]} for {arr[position - 1]}")
            arr[position] = arr[position - 1]
            print(arr)
            print("=" * 100)
            position -= 1
        arr[position] = current
    return arr
def generate_random_array():
    array_list = []
    len_list = int(input("Enter the number of elements in the list: "))
    while len(len_list) > len(array_list):
        item = random.randint(1, 100)
        if item not in array_list:
            array_list.append(item)
    return array_list
def main():
    alist = generate_random_array()
    print(f"List to be sorted using Insertion Sort: {alist}")
    sorted_list = insertion_sort(alist)
    print(f"Final Sorted List: {sorted_list}")
if __name__ == "__main__":
    main()