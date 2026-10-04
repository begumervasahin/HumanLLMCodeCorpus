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
    len_list = input("Banyaknya list: ")
    i = int(len_list)
    while len(array_list) < i:
        item_list = randint(1, 100)
        if item_list not in array_list:
            array_list.append(item_list)
    return array_list
def main():
    alist = randomArray()
    print("List yang akan di sorted menggunakan metode INSERTION SORT adalah : {}".format(alist))
    sorted_list = insertionSort(alist)
    print("Final Sorted List : {}".format(sorted_list))
if __name__ == "__main__":
    main()