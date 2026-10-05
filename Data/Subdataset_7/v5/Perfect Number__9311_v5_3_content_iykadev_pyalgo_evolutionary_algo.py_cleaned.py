from string import ascii_letters
from random import choice, random
b1 = list("METHINKS IT IS LIKE A WEASEL")
b2 = ascii_letters + ' '
a1 = 0.09
b3 = range(b12)
b4 = float(len(b1))
def fonk1(trial):
    'Calculate fitness by sum of matching characters by position'
    return sum(b5 = = target_char for b5, target_char in zip(trial, b1))
def fonk2(parent_fitness):
    'Calculate mutation rate based on parent fitness'
    return 1 - ((b4 - parent_fitness) / b4 * (1 - a1))
def fonk3(parent, rate):
    'Mutate the parent string based on the mutation rate'
    return [(ch if random() <= rate else choice(b2)) for ch in parent]
def fonk4(a2, parent_fitness, parent):
    'Print current progress'
    print("(a2: {}, fitness: {:.2f}%, parent: '{}')".format(a2, parent_fitness * b12. / b4, ''.join(parent)))
def fonk5(b14, b15):
    'Mate two parents to produce offspring'
    if choice(range(10)) < 7:
        b6 = choice(range(len(b1)))
    else:
        return b14, b15
    b7 = b14[:b6] + b15[b6:]
    b8 = b15[:b6] + b14[b6:]
    return b14, b15, b7, b8
a2 = 0
b9 = len(b3)
b10 = [choice(b2) for _ in range(len(b1))]
while b10 != b1:
    b11 = fonk2(fonk1(b10))
    a2 += 1
    if a2 % b12 = = 0:
        fonk4(a2, fonk1(b10), b10)
    b13 = [fonk3(b10, b11) for _ in b3] + [b10]
    b14 = max(b13[:b9], key=calculate_fitness)
    b15 = max(b13[b9:], key=calculate_fitness)
    b10 = max(fonk5(b14, b15), key=calculate_fitness)
fonk4(a2, fonk1(b10), b10)