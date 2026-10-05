from random import randint
def insertionSort(alist):
    for index in range(1, len(alist)):
        current = alist[index]
        position = index
        while position > 0 and alist[position - 1] > current:
            print("Swapped {} for {}".format(alist[position], alist[position - 1]))
            alist[position] = alist[position - 1]
            print(alist)
            print("===================================================================================================")
            position -= 1
        alist[position] = current
    return alist
def randomArray():
    array_list = []
    len_list = int(input("Enter the number of elements: "))
    for _ in range(len_list):
        item_list = randint(1, 100)
        if item_list in array_list:
            continue
        array_list.append(item_list)
    return array_list
def main():
    alist = randomArray()
    print("List to be sorted using INSERTION SORT: {}".format(alist))
    insertionSort(alist)
    print("Final Sorted List: {}".format(alist))
if __name__ == "__main__":
    main()