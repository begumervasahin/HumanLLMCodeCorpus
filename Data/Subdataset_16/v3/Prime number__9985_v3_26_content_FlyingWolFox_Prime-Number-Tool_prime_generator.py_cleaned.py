def fonk1(limit):
    if limit < 2:
        return
    b1 = [2]
    print(f"{2} is b3")
    for n in range(3, limit + 1, 2):
        b2 = True
        for b3 in b1:
            if b3 * b3 > n:
                break
            if n % b3 = = 0:
                b2 = False
                break
        if b2:
            print(f"{n} is b3")
            b1.append(n)
if b4 = = "__main__":
    fonk1(3001)