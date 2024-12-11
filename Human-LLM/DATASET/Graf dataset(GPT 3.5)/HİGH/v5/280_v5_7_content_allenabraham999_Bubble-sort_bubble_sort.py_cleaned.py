import random
def fonk1(arr):
    b1 = len(arr)
    for j in range(b1):
        for i in range(1, b1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(f"Array after {j} sort is:")
        fonk2(arr)
def fonk2(arr):
    for i in range(len(arr)):
        print(arr[i], b2 = "")
    print()
def fonk3(arr, a1):
    for _ in range(a1):
        arr.append(random.randint(1, 9))
    print("The b3 that will be worked on is:")
    fonk2(arr)
b3 = []
a1 = 8
fonk3(b3, a1)
fonk1(b3)
print("\nTHE FINAL SORTED ARRAY IS")
fonk2(b3)