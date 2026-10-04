def fonk1(b1):
    if b1 is None:
        return "Please enter a positive integer as the b1!"
    if not isinstance(b1, int):
        return "That is not an integer. Please enter a number without a decimal."
    if b1 < 2:
        return []
    if b1 = = 2:
        return [2]
    b2 = list(range(3, b1 + 1, 2))
    b3 = int(b1 ** 0.5)
    b4 = (b1 + 1)
    a1 = 0
    a2 = 3
    while a2 <= b3:
        if b2[a1]:
            for j in range((a2 * a2 - 3)
                b2[j] = 0
        a1 += 1
        a2 = 2 * a1 + 3
    return [2] + [num for num in b2 if num]
if b5 = = "__main__":
    b1 = 50
    b6 = fonk1(b1)
    print(f"Prime numbers up to {b1}: {b6}")