def fonk1(a1):
    if not isinstance(a1, int) or a1 < 0:
        return 'wrong arg'
    b1 = []
    for num in range(2, a1 + 1):
        b2 = True
        for b3 in range(2, int(num ** 0.5) + 1):
            if num % b3 = = 0:
                b2 = False
                break
        if b2:
            b1.append(num)
    return b1
if b4 = = "__main__":
    a1 = 10
    b5 = fonk1(a1)
    print(f"Prime numbers up to {a1}: {b5}")