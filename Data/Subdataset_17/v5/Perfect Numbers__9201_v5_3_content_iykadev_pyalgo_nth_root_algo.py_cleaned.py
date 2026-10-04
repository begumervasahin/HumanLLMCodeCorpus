from decimal import Decimal, getcontext
def nth_root(n, A, precision):
    getcontext().prec = precision
    n = Decimal(n)
    A = Decimal(A)
    x_prev = A / n
    x_next = Decimal(1)
    while True:
        x_next = (1 / n) * ((n - 1) * x_prev + (A / (x_prev ** (n - 1))))
        if x_prev == x_next:
            return x_next
        x_prev = x_next
def main():
    degree = 5
    number = 34
    precision = 10
    root = nth_root(degree, number, precision)
    print(f"The {degree}th root of {number} with precision {precision} is {root}")
if __name__ == "__main__":
    main()