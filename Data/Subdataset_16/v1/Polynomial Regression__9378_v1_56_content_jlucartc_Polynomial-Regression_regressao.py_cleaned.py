import sympy as sp
import numpy as np
def fonk1(b8, b6):
    a1 = 0
    for i in range(len(b8)):
        a1 += b8[i] * (b6 ** (len(b8) - (i + 1)))
    return a1
def fonk2(b4):
    try:
        float(b4)
        return True
    except ValueError:
        return False
def fonk3(b1 = 'data.csv'):
    b2 = []
    b3 = []
    with open(b1, 'r') as f:
        for line in f:
            b4 = line.split(',')
            if fonk2(b4[0]) and fonk2(b4[1]):
                b2.append(float(b4[0]))
                b3.append(float(b4[1].strip()))
    return b2, b3
def fonk4():
    b5 = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "))
    if b5 > 24:
        print("\b5\b5------------------\b5  Ordem invÃ¡lida  \b5------------------\b5\b5")
        return
    b6 = sp.symbols('b6')
    b7 = [sp.symbols(chr(i)) for i in range(97, 123)]
    b8 = b7[:b5+1]
    b2, b3 = fonk3()
    b9 = fonk1(b8, b6)
    b10 = sum((b3[i] - b9.subs(b6, b2[i]))**2 for i in range(len(b2)))
    b11 = [sp.diff(b10, b8[i]) for i in range(len(b8))]
    b12 = sp.solve(b11, b8)
    b13 = b9.subs(b12)
    print("Modelo: ", b13)
if b14 = = "__main__":
    fonk4()