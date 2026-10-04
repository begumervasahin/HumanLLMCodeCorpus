import sympy as sp
import numpy as np
def fonk1(b9, b7):
    a1 = 0
    b1 = len(b9)
    for i in range(b1):
        a1 += b9[i] * (b7 ** (b1 - (i + 1)))
    return a1
def fonk2(b5):
    try:
        float(b5)
        return True
    except ValueError:
        return False
def fonk3(b2 = 'data.csv'):
    b3 = []
    b4 = []
    with open(b2, 'r') as f:
        for line in f:
            b5 = line.split(',')
            if fonk2(b5[0]) and fonk2(b5[1]):
                b3.append(float(b5[0]))
                b4.append(float(b5[1].strip()))
    return b3, b4
def fonk4():
    b6 = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "))
    if b6 > 24:
        print("\b6\b6------------------\b6  Ordem invÃ¡lida  \b6------------------\b6\b6")
        return
    b7 = sp.symbols('b7')
    b8 = [sp.symbols(chr(i)) for i in range(97, 123)]
    b9 = b8[:b6+1]
    b3, b4 = fonk3()
    b10 = fonk1(b9, b7)
    b11 = sum((b4[i] - b10.subs(b7, b3[i]))**2 for i in range(len(b3)))
    b12 = [sp.diff(b11, b9[i]) for i in range(len(b9))]
    b13 = sp.solve(b12, b9)
    b14 = b10.subs(b13)
    print("Modelo: ", b14)
if b15 = = "__main__":
    fonk4()