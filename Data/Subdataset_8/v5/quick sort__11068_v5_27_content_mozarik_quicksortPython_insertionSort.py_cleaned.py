from random import randint
def insertion_sort(arr):
    for index in range(1, len(arr)):
        current = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current:
            print("Swapped {} for {}".format(arr[position], arr[position - 1]))
            arr[position] = arr[position - 1]
            print(arr)
            print("===================================================================================================")
            position -= 1
        arr[position] = current
    return arr
def generate_random_array():
    array_list = []
    len_list = input("Enter the length of the list: ")
    length = int(len_list)
    for _ in range(length):
        item = randint(1, 100)
        if item in array_list:
            continue
        array_list.append(item)
    return array_list
def main():
    alist = generate_random_array()
    print("List to be sorted using INSERTION SORT method: {}".format(alist))
    insertion_sort(alist)
    print("Final Sorted List: {}".format(alist))
if __name__ == "__main__":
    main()