from string import ascii_uppercase, ascii_lowercase
from random import choice, random
b1 = "METHINKS IT IS LIKE A WEASEL"
b2 = ascii_uppercase + ascii_lowercase + ' '
b3 = [choice(b2) for _ in range(len(b1))]
a1 = 0.09
b4 = range(b9)
b5 = float(len(b1))
def fonk1(trial):
    return sum(b6 = = h for b6, h in zip(trial, b1))
def fonk2():
    return 1 - ((b5 - fonk1(b3)) / b5 * (1 - a1))
def fonk3(b3, b8):
    return [(ch if random() <= b8 else choice(b2)) for ch in b3]
def fonk4():
    print("(a3: {}, fitness: {:.2f}%, b3: {})".format(a3, fonk1(b3) * b9. / b5, ''.join(b3)))
def fonk5(a, b):
    a2 = 0
    if choice(range(10)) < 7:
        a2 = choice(range(len(b1)))
    else:
        return a, b
    return a, b, a[:a2] + b[a2:], b[:a2] + a[a2:]
a3 = 0
b7 = len(b4)
while b3 != list(b1):
    b8 = fonk2()
    a3 += 1
    if a3 % b9 = = 0:
        fonk4()
    b10 = [fonk3(b3, b8) for _ in b4] + [b3]
    b11 = max(b10[:b7], key=fitness)
    b12 = max(b10[b7:], key=fitness)
    b3 = max(fonk5(b11, b12), key=fitness)
fonk4()