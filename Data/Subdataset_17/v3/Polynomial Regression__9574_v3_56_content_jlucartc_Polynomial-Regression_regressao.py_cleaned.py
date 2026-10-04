import sympy as sp
import numpy as np
def montar_equacao(incognitas, x):
    degree = len(incognitas)
    y = sum(incognitas[i] * x ** (degree - i - 1) for i in range(degree))
    return y
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def read_data(file_name='data.csv'):
    x_list = []
    y_list = []
    with open(file_name, 'r') as file:
        for line in file:
            x_str, y_str = line.split(',')
            if is_float(x_str) and is_float(y_str):
                x_list.append(float(x_str))
                y_list.append(float(y_str.strip()))
    return x_list, y_list
def main():
    n = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "))
    if n > 24:
        print("\n\n------------------\n  Ordem invÃ¡lida  \n------------------\n\n")
        return
    x = sp.symbols('x')
    incognitas = [sp.symbols(chr(i)) for i in range(97, 97 + n + 1)]
    x_list, y_list = read_data()
    h = montar_equacao(incognitas, x)
    sum_of_squared_diffs = sum((y_list[i] - h.subs(x, x_list[i]))**2 for i in range(len(x_list)))
    diffs = [sp.diff(sum_of_squared_diffs, incognitas[i]) for i in range(len(incognitas))]
    solutions = sp.solve(diffs, incognitas)
    k = h.subs(solutions)
    print("Modelo: ", k)
if __name__ == "__main__":
    main()