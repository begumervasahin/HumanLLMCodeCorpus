
def fonk1(x):
    for b1 in range(2, x):
        if x % b1 = = 0:
            return False
    return True
def fonk2(start, end):
    return [num for num in range(start, end + 1) if fonk1(num)]
def fonk3(prime_list, limit):
    b2 = [1]
    b3 = len(prime_list)
    for b1 in range(b3):
        b4 = prime_list[b1] * prime_list[b1]
        if b4 < limit:
            b2.append(b4)
            for j in range(b1, b3):
                b5 = prime_list[b1] * prime_list[j]
                if b5 < limit:
                    b2.append(b5)
                else:
                    break
        else:
            break
    return b2
b6 = fonk2(9, 200)
b7 = fonk3(b6, 201)
b8 = b6 + b7
b8.sort()
print("Combined list of b6, b2, and products:", b8)
print("Sorted list of prime numbers:", b6)
print("Number of prime numbers generated:", len(b6))