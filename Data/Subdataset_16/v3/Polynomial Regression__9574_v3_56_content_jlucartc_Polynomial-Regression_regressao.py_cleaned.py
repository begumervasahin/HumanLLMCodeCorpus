import sympy as sp
import numpy as np
def fonk1(b9, b8):
    b1 = len(b9)
    b2 = sum(b9[i] * b8 ** (b1 - i - 1) for i in range(b1))
    return b2
def fonk2(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def fonk3(b3 = 'data.csv'):
    b4 = []
    b5 = []
    with open(b3, 'r') as file:
        for line in file:
            x_str, b6 = line.split(',')
            if fonk2(x_str) and fonk2(b6):
                b4.append(float(x_str))
                b5.append(float(b6.strip()))
    return b4, b5
def fonk4():
    b7 = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "))
    if b7 > 24:
        print("\b7\b7------------------\b7  Ordem invÃ¡lida  \b7------------------\b7\b7")
        return
    b8 = sp.symbols('b8')
    b9 = [sp.symbols(chr(i)) for i in range(97, 97 + b7 + 1)]
    b4, b5 = fonk3()
    b10 = fonk1(b9, b8)
    b11 = sum((b5[i] - b10.subs(b8, b4[i]))**2 for i in range(len(b4)))
    b12 = [sp.diff(b11, b9[i]) for i in range(len(b9))]
    b13 = sp.solve(b12, b9)
    b14 = b10.subs(b13)
    print("Modelo: ", b14)
if b15 = = "__main__":
    fonk4()