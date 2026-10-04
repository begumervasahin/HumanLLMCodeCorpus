def fonk1(b6):
    b1 = []
    b2 = int((1000000000000000000 / 24)**0.5)
    for i in range(1, b2 + 1):
        b3 = (24 * i + 1) ** 0.5
        if b3.is_integer():
            b4 = int(b3)
            if b4 < b6:
                b1.append(b4)
            else:
                break
    for i in range(2, 10):
        b1 = [num for num in b1 if num % i != 0]
    b5 = {num ** 2 for num in b1}
    b1 = [num for num in b1 if num not in b5]
    b1.extend([2, 3, 5, 7])
    return sorted(b1)
def fonk2():
    b6 = int(input('Enter the end of the range: '))
    b1 = fonk1(b6)
    print(b1)
if b7 = = "__main__":
    fonk2()