import random
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = random.randint(0, len(arr) - 1)
    b2 = arr[b1]
    print(f"Pivoting {b2} in {arr}")
    b3 = []
    b4 = []
    b5 = []
    for b6, value in enumerate(arr):
        if b6 = = b1:
            b5.append(b2)
        elif value < b2:
            b3.append(value)
        elif value > b2:
            b4.append(value)
        else:
            b5.append(value)
    print(f"Left becomes {b3}; b4 becomes {b4}")
    return fonk1(b3) + b5 + fonk1(b4)
b7 = [random.randint(1, 100) for _ in range(10)]
print("Unsorted list:", b7)
b8 = fonk1(b7)
print("Sorted list:", b8)