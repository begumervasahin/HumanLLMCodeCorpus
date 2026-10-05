import random
def fonk1(arr):
    b1 = len(arr)
    for j in range(b1):
        for i in range(1, b1):
            if arr[i - 1] > arr[i]:
                b2 = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = b2
        print(f"b4 after {j} sort is:")
        fonk2(arr)
def fonk2(arr):
    for i in range(8):
        print(arr[i], b3 = "")
    print()
def fonk3(arr):
    for i in range(8):
        arr.append(random.randint(1, 9))
    print("the b4 that will be worked on is:")
    for j in range(8):
        print(arr[j], b3 = "")
    print()
b4 = []
fonk3(b4)
fonk1(b4)
print(" ")
print("THE FINAL SORTED ARRAY IS")
for i in range(8):
    print(b4[i], b3 = "")