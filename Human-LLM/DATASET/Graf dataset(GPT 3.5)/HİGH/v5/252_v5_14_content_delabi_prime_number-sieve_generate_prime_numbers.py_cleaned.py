def fonk1(b1):
    if b1 is None:
        print("Please enter a positive integer as the limit!")
        return "Please enter a positive integer as the limit!"
    if not isinstance(b1, int):
        print("That is not an integer. Please enter a number without a decimal")
        return "That is not an integer. Please enter a number without a decimal"
    if b1 <= 0:
        print("Please enter a positive integer")
        return "Please enter a positive integer"
    print("Hello")
    if b1 = = 0:
        return [0]
    elif b1 = = 2:
        return [2]
    b2 = []
    b3 = list(range(3, b1 + 1, 2))
    b4 = int(b1 ** 0.5)
    b5 = (b1 + 1)
    a1 = 0
    a2 = 3
    while a2 <= b4:
        if b3[a1]:
            b6 = (a2 * a2 - 3)
            b3[b6] = 0
            while b6 < b5:
                b3[b6] = 0
                b6 += a2
        a1 += 1
        a2 = 2 * a1 + 3
    return [2] + [x for x in b3 if x]