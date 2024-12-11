from random import randint
def fonk1(arr):
    for index in range(1, len(arr)):
        b1 = arr[index]
        b2 = index
        while b2 > 0 and arr[b2 - 1] > b1:
            print("Swapped {} for {}".format(arr[b2], arr[b2 - 1]))
            arr[b2] = arr[b2 - 1]
            print(arr)
            print("===================================================================================================")
            b2 -= 1
        arr[b2] = b1
    return arr
def fonk2():
    b3 = []
    b4 = input("Enter the b5 of the list: ")
    b5 = int(b4)
    for _ in range(b5):
        b6 = randint(1, 100)
        if b6 in b3:
            continue
        b3.append(b6)
    return b3
def fonk3():
    b7 = fonk2()
    print("List to be sorted using INSERTION SORT method: {}".format(b7))
    fonk1(b7)
    print("Final Sorted List: {}".format(b7))
if b8 = = "__main__":
    fonk3()