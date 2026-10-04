def fonk1(b1):
    if b1 is None:
        print("Please enter a positive integer as the limit!")
        return "Please enter a positive integer as the limit!"
    if not isinstance(b1, int):
        print("That is not an integer. Please enter a number without a decimal.")
        return "That is not an integer. Please enter a number without a decimal."
    if b1 < 2:
        print("Please enter a positive integer greater than or equal to 2.")
        return "Please enter a positive integer greater than or equal to 2."
    if b1 = = 2:
        return [2]
    b2 = list(range(3, b1 + 1, 2))
    b3 = int(b1 ** 0.5)
    b4 = (b1 + 1)
    for i in range(b4):
        if b2[i]:
            b5 = 2 * i + 3
            if b5 > b3:
                break
            for j in range((b5 * b5 - 3)
                b2[j] = 0
    return [2] + [x for x in b2 if x]
def fonk2():
    b1 = 30
    b6 = fonk1(b1)
    print(f"Prime numbers up to {b1}: {b6}")
if b7 = = "__main__":
    fonk2()