import numpy as np
from sympy import symbols, diff, solve
from math import *
def fonk1(b7, b3):
    a1 = 0
    for b12 in range(len(b7)):
        a1 += b7[b12] * (b3 ** (len(b7) - (b12 + 1)))
    return a1
def fonk2(b6):
    try:
        float(b6)
        return True
    except ValueError:
        return False
def fonk3():
    a2 = 24
    b1 = 'abcdefghijklmnopqrstuvwxyz'
    b2 = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "))
    if b2 > a2:
        print("\b2\b2------------------\b2  Ordem invÃ¡lida  \b2------------------\b2\b2")
        return
    b3 = symbols('b3')
    b4 = []
    b5 = []
    with open('data.csv', 'r') as file:
        for line in file:
            b6 = line.strip().split(',')
            if len(b6) != 2:
                continue
            if fonk2(b6[0]) and fonk2(b6[1]):
                b4.append(float(b6[0]))
                b5.append(float(b6[1]))
    b7 = [symbols(b1[b12]) for b12 in range(b2 + 1)]
    b8 = fonk1(b7, b3)
    b9 = sum((b5[b12] - b8.subs(b3, b4[b12])) ** 2 for b12 in range(len(b4)))
    b10 = [diff(b9, b7[b12]) for b12 in range(len(b7))]
    b11 = []
    for b12 in range(len(b7)):
        if b12 = = 0:
            b13 = solve(b10[-1], b7[-1])[0]
            b10[-1] = b13
            b11.append((b7[-1], b13))
        else:
            b13 = solve(b10[-(b12 + 1)].subs(b11), b7[-(b12 + 1)])[0]
            b10[-(b12 + 1)] = b13
            b11.append((b7[-(b12 + 1)], b13))
    b14 = sum(b10[b12] * b3 ** (len(b7) - (b12 + 1)) for b12 in range(len(b7)))
    print("Modelo:", b14)
if b15 = = "__main__":
    fonk3()