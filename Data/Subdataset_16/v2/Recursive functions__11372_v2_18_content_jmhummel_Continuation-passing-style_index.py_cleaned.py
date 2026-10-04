def fonk1(b1):
    if b1 = = 0:
        return 1
    return b1 * fonk1(b1 - 1)
def fonk2(b1, cont):
    if b1 = = 0:
        return cont(1)
    return fonk2(b1 - 1, lambda value: cont(b1 * value))
def fonk3(b1):
    return b1
def fonk4(f, *args):
    b2 = f(*args)
    while callable(b2):
        b2 = b2()
    return b2
def fonk5(b1, cont):
    if b1 = = 0:
        return cont(1)
    return lambda: fonk5(b1 - 1, lambda value: lambda: cont(b1 * value))
def fonk6(b1):
    if b1 <= 2:
        return 1
    return fonk6(b1 - 1) + fonk6(b1 - 2)
def fonk7(b1, cont):
    if b1 <= 2:
        return cont(1)
    return fonk7(b1 - 1, lambda value1: fonk7(b1 - 2, lambda value2: cont(value1 + value2)))
def fonk8(b1, cont):
    if b1 <= 2:
        return cont(1)
    return lambda: fonk8(b1 - 1, lambda value1: fonk8(b1 - 2, lambda value2: cont(value1 + value2)))
def fonk9():
    print("Testing Factorial Functions")
    try:
        print(fonk1(10))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fonk2(10, end_cont))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fonk4(fonk5(10, end_cont)))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    print("\nTesting Fibonacci Functions")
    try:
        print(fonk6(10))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fonk7(10, end_cont))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fonk4(fonk8(10, end_cont)))
    except RecursionError as e:
        print(f'RecursionError: {e}')
if b3 = = '__main__':
    fonk9()