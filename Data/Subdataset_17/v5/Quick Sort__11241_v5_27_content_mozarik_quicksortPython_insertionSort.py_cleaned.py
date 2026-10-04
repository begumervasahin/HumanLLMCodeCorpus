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
def generate_random_array(length):
    array_list = []
    while len(array_list) < length:
        item = random.randint(1, 100)
        if item not in array_list:
            array_list.append(item)
    return array_list
def main():
    try:
        len_list = int(input("Enter the number of elements in the list: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    alist = generate_random_array(len_list)
    print(f"List to be sorted using Insertion Sort: {alist}")
    sorted_list = insertion_sort(alist)
    print(f"Final Sorted List: {sorted_list}")
if __name__ == "__main__":
    main()