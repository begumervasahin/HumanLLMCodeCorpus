def fonk1(b1):
    if b1 is not None:
        print("Starting prime number generation...")
        if b1 > 0:
            if isinstance(b1, int):
                if b1 = = 0:
                    return [0]
                elif b1 = = 2:
                    return [2]
                elif b1 < 2:
                    return []
                b2 = list(range(3, b1 + 1, 2))
                b3 = int(b1 ** 0.5)
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
            print("Error: The input is not an integer. Please enter a whole number.")
            return "Error: The input is not an integer. Please enter a whole number."
        print("Error: Please enter a positive integer.")
        return "Error: Please enter a positive integer."
    print("Error: Please enter a positive integer as the limit.")
    return "Error: Please enter a positive integer as the limit."
b1 = 20
print(fonk1(b1))