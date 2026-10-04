def solve_linear_equation_cramers_rule():
    print("SOLVE A LINEAR EQUATION BY CRAMER'S RULE OF DISCRIMINANTS")
    print("Equation no. 1")
    a = int(input("Enter the coefficient 'a': "))
    b = int(input("Enter the coefficient 'b': "))
    c = int(input("Enter the constant 'c': "))
    print_equation(a, b, c)
    print("----------------------------")
    print("Equation no. 2")
    k = int(input("Enter the coefficient 'k': "))
    l = int(input("Enter the coefficient 'l': "))
    m = int(input("Enter the constant 'm': "))
    print_equation(k, l, m)
    print("--------------------------------------------")
    print("The equations will be solved by Cramer's rule.")
    d = a * l - b * k
    dx = c * l - b * m
    dy = a * m - c * k
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