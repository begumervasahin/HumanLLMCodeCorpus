import numpy as np
from sympy import symbols, diff, solve
from math import *
def montar_equacao(incognitas, x):
    y = 0
    for i in range(len(incognitas)):
        y += incognitas[i] * (x ** (len(incognitas) - (i + 1)))
    return y
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def main():
    MAX_ORDER = 24
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    n = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "))
    if n > MAX_ORDER:
        print("\n\n------------------\n  Ordem invÃ¡lida  \n------------------\n\n")
        return
    x = symbols('x')
    x_list = []
    y_list = []
    with open('data.csv', 'r') as file:
        for line in file:
            s = line.strip().split(',')
            if len(s) != 2:
                continue
            if is_float(s[0]) and is_float(s[1]):
                x_list.append(float(s[0]))
                y_list.append(float(s[1]))
    incognitas = [symbols(ALPHABET[i]) for i in range(n + 1)]
    h = montar_equacao(incognitas, x)
    soma_quadrada_diferencas = sum((y_list[i] - h.subs(x, x_list[i])) ** 2 for i in range(len(x_list)))
    diffs = [diff(soma_quadrada_diferencas, incognitas[i]) for i in range(len(incognitas))]
    rep = []
    for i in range(len(incognitas)):
        if i == 0:
            solved_diff = solve(diffs[-1], incognitas[-1])[0]
            diffs[-1] = solved_diff
            rep.append((incognitas[-1], solved_diff))
        else:
            solved_diff = solve(diffs[-(i + 1)].subs(rep), incognitas[-(i + 1)])[0]
            diffs[-(i + 1)] = solved_diff
            rep.append((incognitas[-(i + 1)], solved_diff))
    k = sum(diffs[i] * x ** (len(incognitas) - (i + 1)) for i in range(len(incognitas)))
    print("Modelo:", k)
if __name__ == "__main__":
    main()