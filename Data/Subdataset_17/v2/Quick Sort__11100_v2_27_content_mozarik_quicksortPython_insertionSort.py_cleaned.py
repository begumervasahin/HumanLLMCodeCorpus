from random import randint
def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and alist[position - 1] > current_value:
            print(f"Swapped {alist[position]} for {alist[position - 1]}")
            alist[position] = alist[position - 1]
            print(alist)
            print("===================================================================================================")
            position -= 1
        alist[position] = current_value
    return alist
def generate_random_array():
    array_list = []
    len_list = int(input("Enter the number of elements in the list: "))
    while len(array_list) < len_list:
        item = randint(1, 100)
        if item not in array_list:
            array_list.append(item)
    return array_list
def main():
    alist = generate_random_array()
    print(f"The list to be sorted using insertion sort is: {alist}")
    sorted_list = insertion_sort(alist)
    print(f"Final Sorted List: {sorted_list}")
if __name__ == "__main__":
    main()