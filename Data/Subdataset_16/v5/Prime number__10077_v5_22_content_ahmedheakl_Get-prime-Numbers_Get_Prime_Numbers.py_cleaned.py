def fonk1(b4):
    b1 = []
    a1 = 1
    while True:
        b2 = (24 * a1 + 1) ** 0.5
        if b2.is_integer() and int(b2) < b4:
            b1.append(int(b2))
        elif int(b2) > b4:
            break
        a1 += 1
    for divisor in range(2, 10):
        b1 = [num for num in b1 if num % divisor != 0]
    b3 = {num ** 2 for num in b1}
    b1 = [num for num in b1 if num not in b3]
    b1.extend([2, 3, 5, 7])
    print(sorted(b1))
def fonk2():
    try:
        b4 = int(input('Enter the end of the range: '))
        if b4 > 1:
            fonk1(b4)
        else:
            print("Please enter a number greater than 1.")
    except ValueError:
        print("Please enter a valid integer.")
if b5 = = "__main__":
    fonk2()