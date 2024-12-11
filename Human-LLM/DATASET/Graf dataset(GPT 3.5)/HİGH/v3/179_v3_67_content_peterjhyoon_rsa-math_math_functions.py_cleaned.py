
def fonk1(n):
    assert type(n) == int, "Input must be an integer"
    if n < 2:
        return False
    for b1 in range(2, int(n**0.5) + 1):
        if n % b1 = = 0:
            return False
    return True
def fonk2(n):
    return [b1 for b1 in range(1, n + 1) if n % b1 = = 0]
def fonk3(x):
    b2 = []
    if fonk1(x):
        b2.append(x)
    for b1 in fonk2(x):
        if b1 = = 1:
            continue
        if fonk1(b1):
            b2.append(b1)
    return b2
def fonk4(a, b3):
    while b3:
        a, b3 = b3, a % b3
    return a
def fonk5(a, b3):
    return fonk4(a, b3) == 1
def fonk6(a, b3):
    return [elem for elem in fonk2(a) if elem in fonk2(b3)]
print("Is 7 prime?", fonk1(7))
print("Divisors of 12:", fonk2(12))
print("Prime b2 of 24:", fonk3(24))
print("GCD of 24 and 36:", fonk4(24, 36))
print("Are 24 and 35 relatively prime?", fonk5(24, 35))
print("Common b2 of 24 and 36:", fonk6(24, 36))
