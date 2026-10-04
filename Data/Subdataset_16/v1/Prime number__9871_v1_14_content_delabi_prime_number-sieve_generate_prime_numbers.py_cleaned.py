def fonk1(b1):
    if b1 is not None:
        print("Hallo")
        if b1 > 0:
            if isinstance(b1, int):
                if b1 = = 0:
                    return [0]
                elif b1 = = 2:
                    return [2]
                elif b1 < 2:
                    return []
                b2 = list(range(3, b1 + 1, 2))
                b3 = b1 ** 0.5
                b4 = (b1 + 1)
                a1 = 0
                a2 = 3
                while a2 <= b3:
                    if b2[a1]:
                        b5 = (a2 * a2 - 3)
                        b2[b5] = 0
                        while b5 < b4:
                            b2[b5] = 0
                            b5 += a2
                    a1 += 1
                    a2 = 2 * a1 + 3
                return [2] + [x for x in b2 if x]
            print("That is not an integer. Please enter a number without a decimal")
            return "That is not an integer. Please enter a number without a decimal"
        print("Please enter a positive integer")
        return "Please enter a positive integer"
    print("Please enter a positive integer as the a3!")
    return "Please enter a positive integer as the a3!"
if b6 = = "__main__":
    a3 = 50
    b7 = fonk1(a3)
    print("Prime numbers up to {}: {}".format(a3, b7))