import random
def fonk1(arr):
    for index in range(1, len(arr)):
        b1 = arr[index]
        b2 = index
        while b2 > 0 and arr[b2 - 1] > b1:
            print(f"Swapped {arr[b2]} for {arr[b2 - 1]}")
            arr[b2] = arr[b2 - 1]
            print(arr)
            print("=" * 100)
            b2 -= 1
        arr[b2] = b1
    return arr
def fonk2():
    b3 = []
    b4 = int(input("Enter the number of elements in the list: "))
    while len(b4) > len(b3):
        b5 = random.randint(1, 100)
        if b5 not in b3:
            b3.append(b5)
    return b3
def fonk3():
    b6 = fonk2()
    print(f"List to be sorted using Insertion Sort: {b6}")
    b7 = fonk1(b6)
    print(f"Final Sorted List: {b7}")
if b8 = = "__main__":
    fonk3()