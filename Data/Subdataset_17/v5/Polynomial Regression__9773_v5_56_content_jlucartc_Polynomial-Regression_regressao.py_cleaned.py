import numpy as np
from sympy import symbols, diff, solve
from math import *
def montar_equacao(coefs, x):
    y = sum(coefs[i] * (x ** (len(coefs) - (i + 1))) for i in range(len(coefs)))
    return y
def is_float(value):
    try:
        float(value)
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
    x_list, y_list = [], []
    with open('data.csv', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) == 2 and is_float(values[0]) and is_float(values[1]):
                x_list.append(float(values[0]))
                y_list.append(float(values[1]))
    coefs = [symbols(ALPHABET[i]) for i in range(n + 1)]
    polynomial = montar_equacao(coefs, x)
    squared_diff_sum = sum((y - polynomial.subs(x, x_val)) ** 2 for x_val, y in zip(x_list, y_list))
    derivatives = [diff(squared_diff_sum, coef) for coef in coefs]
    solutions = []
    for i in range(len(coefs)):
        if i == 0:
            solved_value = solve(derivatives[-1], coefs[-1])[0]
            derivatives[-1] = solved_value
            solutions.append((coefs[-1], solved_value))
        else:
            solved_value = solve(derivatives[-(i + 1)].subs(solutions), coefs[-(i + 1)])[0]
            derivatives[-(i + 1)] = solved_value
            solutions.append((coefs[-(i + 1)], solved_value))
    final_model = sum(derivatives[i] * x ** (len(coefs) - (i + 1)) for i in range(len(coefs)))
    print("Modelo:", final_model)
if __name__ == "__main__":
    main()