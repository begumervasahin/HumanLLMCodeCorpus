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
def fonk2(length):
    b3 = []
    while len(b3) < length:
        b4 = random.randint(1, 100)
        if b4 not in b3:
            b3.append(b4)
    return b3
def fonk3():
    try:
        b5 = int(input("Enter the number of elements in the list: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    b6 = fonk2(b5)
    print(f"List to be sorted using Insertion Sort: {b6}")
    b7 = fonk1(b6)
    print(f"Final Sorted List: {b7}")
if b8 = = "__main__":
    fonk3()