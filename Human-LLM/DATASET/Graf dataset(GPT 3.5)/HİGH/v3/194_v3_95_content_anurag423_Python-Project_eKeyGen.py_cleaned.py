def fonk1(n):
    return [b1 for b1 in range(2, n) if n % b1 = = 0]
def fonk2(a2):
    return [b1 for b1 in range(2, a2)]
def fonk3(possible_values, factors):
    b2 = possible_values[:]
    for value in possible_values:
        for b3 in factors:
            if value % b3 = = 0:
                b2.remove(value)
                break
    return b2
def fonk4(a1, a2):
    b4 = fonk1(a1)
    b5 = fonk1(a2)
    b6 = fonk2(a2)
    b6 = fonk3(b6, b4)
    b6 = fonk3(b6, b5)
    return b6
a1 = 35
a2 = 24
print("Possible values for e:", fonk4(a1, a2))