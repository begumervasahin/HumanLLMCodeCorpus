import random
def fonk1(arr):
    b1 = len(arr)
    for j in range(b1):
        for i in range(1, b1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(f"Array after {j + 1} pass:")
        fonk2(arr)
def fonk2(arr):
    for elem in arr:
        print(elem, b2 = " ")
    print()
def fonk3(arr, b3 = 8, lower_bound=1, upper_bound=9):
    for _ in range(b3):
        arr.append(random.randint(lower_bound, upper_bound))
    print("The initial b4 is:")
    fonk2(arr)
def fonk4():
    b4 = []
    fonk3(b4)
    fonk1(b4)
    print("\nThe final sorted b4 is:")
    fonk2(b4)
if b5 = = "__main__":
    fonk4()