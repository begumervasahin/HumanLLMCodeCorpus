def fonk1(x):
    if x < 2:
        return None
    for b1 in range(2, int(x ** 0.5) + 1):
        if x % b1 = = 0:
            return None
    return x
def fonk2():
    b2 = list(filter(None, map(is_prime, range(9, 201))))
    b3 = [1]
    for b1, prime_i in enumerate(b2):
        b4 = prime_i * prime_i
        if b4 < 201:
            b3.append(b4)
            for j in range(b1 + 1, len(b2)):
                b5 = prime_i * b2[j]
                if b5 < 201:
                    b3.append(b5)
                else:
                    break
        else:
            break
    b6 = sorted(set(b2 + b3))
    return b6
def fonk3():
    b7 = fonk2()
    print(b7)
if b8 = = "__main__":
    fonk3()