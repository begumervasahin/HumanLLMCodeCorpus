def solve_linear_equation_cramers_rule():
    print("SOLVE A LINEAR EQUATION BY CRAMER'S RULE OF DISCRIMINANTS")
    print("Equation no. 1")
    a = get_coefficient("a")
    b = get_coefficient("b")
    c = get_coefficient("c")
    print_equation(a, b, c)
    print("----------------------------")
    print("Equation no. 2")
    k = get_coefficient("k")
    l = get_coefficient("l")
    m = get_coefficient("m")
    print_equation(k, l, m)
    print("--------------------------------------------")
    print("The equations will be solved by Cramer's rule.")
    d = calculate_determinant(a, b, k, l)
    dx = calculate_determinant(c, b, m, l)
    dy = calculate_determinant(a, c, k, m)
    if d == 0:
        if dx == 0 and dy == 0:
            print("The system has infinitely many solutions.")
        else:
            print("The system has no solution.")
    else:
        x = dx / d
        y = dy / d
        print(f'd = {d}')
        print(f'dx = {dx}')
        print(f'dy = {dy}')
        print(f'x = {x}')
        print(f'y = {y}')
def get_coefficient(name):
    return int(input(f"Enter the coefficient '{name}': "))
def calculate_determinant(a, b, c, d):
    return a * d - b * c
def print_equation(a, b, c):
    equation = []
    if a != 0:
        equation.append(f"{a}x")
    if b != 0:
        if b > 0 and a != 0:
            equation.append(f"+ {b}y")
        else:
            equation.append(f"{b}y")
    equation.append(f"= {c}")
    print(" ".join(equation))
if __name__ == "__main__":
    solve_linear_equation_cramers_rule()