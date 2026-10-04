import random
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = random.randint(0, len(arr) - 1)
    b2 = arr[b1]
    print(f"Pivoting {b2} in {arr}")
    b3 = [x for i, x in enumerate(arr) if x < b2 and i != b1]
    b4 = [x for i, x in enumerate(arr) if x > b2 and i != b1]
    b5 = [x for x in arr if x == b2]
    print(f"Left becomes {b3}; b4 becomes {b4}")
    return fonk1(b3) + b5 + fonk1(b4)
b6 = [random.randint(1, 100) for _ in range(10)]
print("Unsorted list:", b6)
b7 = fonk1(b6)
print("Sorted list:", b7)