import sympy as sp
import numpy as np
def montarEquacao(incognitas, x):
    y = 0
    degree = len(incognitas)
    for i in range(degree):
        y += incognitas[i] * (x ** (degree - (i + 1)))
    return y
def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def read_data(file_name='data.csv'):
    xLista = []
    yLista = []
    with open(file_name, 'r') as f:
        for line in f:
            s = line.split(',')
            if isFloat(s[0]) and isFloat(s[1]):
                xLista.append(float(s[0]))
                yLista.append(float(s[1].strip()))
    return xLista, yLista
def main():
    n = int(input("Digite a ordem da regressÃ£o (ordem mÃ¡xima = 24): "))
    if n > 24:
        print("\n\n------------------\n  Ordem invÃ¡lida  \n------------------\n\n")
        return
    x = sp.symbols('x')
    lista_simbolos = [sp.symbols(chr(i)) for i in range(97, 123)]
    incognitas = lista_simbolos[:n+1]
    xLista, yLista = read_data()
    h = montarEquacao(incognitas, x)
    somaQuadradaDiferencas = sum((yLista[i] - h.subs(x, xLista[i]))**2 for i in range(len(xLista)))
    diffs = [sp.diff(somaQuadradaDiferencas, incognitas[i]) for i in range(len(incognitas))]
    solutions = sp.solve(diffs, incognitas)
    k = h.subs(solutions)
    print("Modelo: ", k)
if __name__ == "__main__":
    main()