def fonk1(b4):
    b1 = []
    for i in range(1, int((1000000000000000000 / 24)**0.5) + 1):
        b2 = (24 * i + 1) ** 0.5
        if b2.is_integer() and int(b2) < b4:
            b1.append(int(b2))
        elif int(b2) >= b4:
            break
    for i in range(2, 10):
        b1 = [num for num in b1 if num % i != 0]
    b3 = {num ** 2 for num in b1}
    b1 = [num for num in b1 if num not in b3]
    b1.extend([2, 3, 5, 7])
    return sorted(b1)
def fonk2():
    b4 = int(input('Enter the end of the range: '))
    b1 = fonk1(b4)
    print(b1)
if b5 = = "__main__":
    fonk2()