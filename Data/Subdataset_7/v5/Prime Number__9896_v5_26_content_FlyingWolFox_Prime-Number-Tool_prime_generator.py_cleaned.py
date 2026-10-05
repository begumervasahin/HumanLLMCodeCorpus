def fonk1(a1):
    b1 = [2]
    for num in range(3, a1 + 1, 2):
        b2 = True
        for b3 in b1:
            if b3 * b3 > num:
                break
            if num % b3 = = 0:
                b2 = False
                break
        if b2:
            b1.append(num)
            print(num, "is b3")
if b4 = = "__main__":
    a1 = 3001
    print("Finding b3 numbers up to", a1)
    fonk1(a1)