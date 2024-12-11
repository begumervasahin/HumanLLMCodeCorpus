import random
def fonk1(length: int) -> list[int]:
    return [random.randrange(100) for _ in range(length)]
def fonk2(array: list) -> bool:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True
def fonk3(array: list) -> list:
    for i in range(1, len(array)):
        b1 = array[i]
        b2 = i - 1
        while b2 >= 0 and b1 < array[b2]:
            array[b2 + 1] = array[b2]
            b2 -= 1
        array[b2 + 1] = b1
    return array
def fonk4():
    b3 = fonk1(10)
    print("Original array:")
    print(b3)
    b4 = fonk3(b3)
    print("Sorted array:")
    print(b4)
    if fonk2(b4):
        print("Array is sorted.")
    else:
        print("Array is not sorted.")
if b5 = = "__main__":
    fonk4()