def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)
def fact_cps(n, cont):
    if n == 0:
        return cont(1)
    return fact_cps(n - 1, lambda value: cont(n * value))
def end_cont(n):
    return n
def trampoline(f, *args):
    result = f(*args)
    while callable(result):
        result = result()
    return result
def fact_cps_thunked(n, cont):
    if n == 0:
        return cont(1)
    return lambda: fact_cps_thunked(n - 1, lambda value: lambda: cont(n * value))
def fib_rec(n):
    if n <= 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)
def fib_cps(n, cont):
    if n <= 2:
        return cont(1)
    return fib_cps(n - 1, lambda value1: fib_cps(n - 2, lambda value2: cont(value1 + value2)))
def fib_cps_thunked(n, cont):
    if n <= 2:
        return cont(1)
    return lambda: fib_cps_thunked(n - 1, lambda value1: fib_cps_thunked(n - 2, lambda value2: cont(value1 + value2)))
def main():
    print("Testing Factorial Functions")
    try:
        print(fact_rec(10))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fact_cps(10, end_cont))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(trampoline(fact_cps_thunked(10, end_cont)))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    print("\nTesting Fibonacci Functions")
    try:
        print(fib_rec(10))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fib_cps(10, end_cont))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(trampoline(fib_cps_thunked(10, end_cont)))
    except RecursionError as e:
        print(f'RecursionError: {e}')
if __name__ == '__main__':
    main()