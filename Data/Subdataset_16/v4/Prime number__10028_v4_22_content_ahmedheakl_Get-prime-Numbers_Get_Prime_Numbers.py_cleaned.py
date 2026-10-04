def fonk1(b5):
    b1 = []
    a1 = b3
    while True:
        b2 = (24 * a1 + b3) ** 0.5
        if b2 % b3 = = 0 and int(b2) < b5:
            b1.append(int(b2))
        elif int(b2) > b5:
            break
        a1 += b3
    for a1 in range(2, 10):
        b1 = [num for num in b1 if num % a1 != 0]
    b4 = [y ** 2 for y in b1]
    b1 = [num for num in b1 if num not in b4]
    b1 += [2, 3, 5, 7]
    print(sorted(b1))
def fonk2():
    try:
        b5 = int(input('Enter the end of the range: '))
        fonk1(b5)
    except ValueError:
        print("Please enter a valid integer.")
if b6 = = "__main__":
    fonk2()