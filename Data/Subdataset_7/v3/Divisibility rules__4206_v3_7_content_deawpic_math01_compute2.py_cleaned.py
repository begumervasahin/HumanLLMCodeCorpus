def fonk1(number):
    if number <= 1:
        return False
    for b1 in range(2, int(number**0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2(start, end):
    b2 = [number for number in range(start, end + 1) if fonk1(number)]
    return b2
def fonk3(b2, limit):
    b3 = [1]
    for i in range(len(b2)):
        b4 = b2[i] * b2[i]
        if b4 < limit:
            b3.append(b4)
            for j in range(i, len(b2)):
                b5 = b2[i] * b2[j]
                if b5 < limit:
                    b3.append(b5)
                else:
                    break
        else:
            break
    return b3
b6 = fonk2(9, 200)
b7 = fonk3(b6, 201)
b8 = sorted(b6 + b7)
print("Combined list of b2, squares, and products:", b8)
print("Sorted list of prime numbers:", b6)
print("Number of prime numbers generated:", len(b6))