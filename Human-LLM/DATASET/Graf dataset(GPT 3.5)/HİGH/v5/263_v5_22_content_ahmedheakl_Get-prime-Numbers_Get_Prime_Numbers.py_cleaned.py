def fonk1(b6):
    b1 = []
    for i in range(b3, b6):
        b2 = (24 * i + b3) ** 0.5
        if b2 % b3 = = 0 and int(b2) < b6:
            b1.append(int(b2))
        elif int(b2) > b6:
            break
    b1 = [num for num in b1 if all(num % i != 0 for i in range(2, 10))]
    b4 = [num ** 2 for num in b1]
    b1 = [num for num in b1 if num not in b4]
    b1.extend([2, 3, 5, 7])
    b1.sort()
    return b1
if b5 = = "__main__":
    b6 = int(input('Enter the end of the range: '))
    b7 = fonk1(b6)
    print(b7)