def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        for j in range(0, b1 - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def fonk2():
    b2 = [100, 2993, 22, 1, 82, 11, 33]
    fonk1(b2)
    print("Sorted:")
    for num in b2:
        print(num, b3 = " ")
if b4 = = "__main__":
    fonk2()