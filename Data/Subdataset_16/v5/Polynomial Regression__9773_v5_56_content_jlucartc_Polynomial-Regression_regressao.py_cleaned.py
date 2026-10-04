import numpy as np
from sympy import symbols, diff, solve
from math import *
def fonk1(b7, b4):
    b1 = sum(b7[b12] * (b4 ** (len(b7) - (b12 + 1))) for b12 in range(len(b7)))
    return b1
def fonk2(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def fonk3():
    a1 = 24
    b2 = 'abcdefghijklmnopqrstuvwxyz'
    b3 = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "))
    if b3 > a1:
        print("\b3\b3------------------\b3  Ordem invÃ¡lida  \b3------------------\b3\b3")
        return
    b4 = symbols('b4')
    x_list, b5 = [], []
    with open('data.csv', 'r') as file:
        for line in file:
            b6 = line.strip().split(',')
            if len(b6) == 2 and fonk2(b6[0]) and fonk2(b6[1]):
                x_list.append(float(b6[0]))
                b5.append(float(b6[1]))
    b7 = [symbols(b2[b12]) for b12 in range(b3 + 1)]
    b8 = fonk1(b7, b4)
    b9 = sum((b1 - b8.subs(b4, x_val)) ** 2 for x_val, b1 in zip(x_list, b5))
    b10 = [diff(b9, coef) for coef in b7]
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
    b14 = sum(b10[b12] * b4 ** (len(b7) - (b12 + 1)) for b12 in range(len(b7)))
    print("Modelo:", b14)
if b15 = = "__main__":
    fonk3()