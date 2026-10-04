import random
def fonk1(arr):
    b1 = len(arr)
    for j in range(b1):
        for i in range(1, b1):
            if arr[i - 1] > arr[i]:
                b2 = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = b2
        print(f"\nArray after {j + 1} sort is:")
        fonk2(arr)
def fonk2(arr):
    for i in range(len(arr)):
        print(arr[i], b3 = " ")
def fonk3(arr):
    for i in range(8):
        arr.append(random.randint(1, 9))
    print("The b4 that will be worked on is:")
    fonk2(arr)
b4 = []
fonk3(b4)
print("\n")
fonk1(b4)
print("\nTHE FINAL SORTED ARRAY IS")
fonk2(b4)