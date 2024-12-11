def fonk1(b1):
    if b1 = = 0:
        return 1
    else:
        return b1 * fonk1(b1-1)
def fonk2(b1, cont):
    if b1 = = 0:
        return cont(1)
    else:
        return fonk2(b1-1, lambda value: cont(b1 * value))
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
    else:
        return lambda: fonk5(
            b1 - 1,
            lambda value: lambda: cont(b1 * value))
def fonk6(b1):
    if b1 <= 2:
        return 1
    else:
        return fonk6(b1-1) + fonk6(b1-2)
def fonk7(b1, cont):
    if b1 <= 2:
        return cont(1)
    else:
        return fonk2(
            b1-1,
            lambda value1: fonk7(
                b1-2,
                lambda value2: cont(value1 + value2)
            )
        )
def fonk8(b1, cont):
    if b1 <= 2:
        return cont(1)
    else:
        return lambda: fonk8(
            b1-1,
            lambda value1: fonk8(
                b1-2,
                lambda value2: cont(value1 + value2)
            )
        )
def fonk9():
    try:
        print(fonk1(1000))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fonk2(1000, end_cont))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fonk4(fonk5(1000, end_cont)))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fonk7(43, end_cont))
    except RecursionError as e:
        print(f'RecursionError: {e}')
    try:
        print(fonk4(fonk8(43, end_cont)))
    except RecursionError as e:
        print(f'RecursionError: {e}')
if b3 = = '__main__':
    fonk9()