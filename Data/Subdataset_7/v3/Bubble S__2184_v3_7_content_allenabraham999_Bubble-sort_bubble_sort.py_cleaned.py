import random
def fonk1(arr):
    b1 = len(arr)
    for pass_num in range(b1):
        for i in range(1, b1 - pass_num):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(f"Array after {pass_num} sort is:")
        fonk2(arr)
def fonk2(arr):
    for i in range(len(arr)):
        print(arr[i], b2 = "")
    print()
def fonk3(arr):
    for i in range(8):
        arr.append(random.randint(1, 9))
    print("The b3 that will be worked on is:")
    fonk2(arr)
b3 = []
fonk3(b3)
fonk1(b3)
print(" ")
print("THE FINAL SORTED ARRAY IS")
fonk2(b3)