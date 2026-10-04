def fonk1(b4, a3, b9, a1):
    b1 = []
    for _ in range(a1):
        b2 = a3 * b4
        b1.append(b2)
        b3 = b4 - b2
        b4 = b3 + b9 * b3
    return round(b4, 2), b1
def fonk2(b4, b9, a1, b7, b8):
    while b7 <= b8:
        b5 = (b7 + b8) / 2
        b6 = b4
        for _ in range(a1):
            b3 = b6 - b5
            b6 = b3 + b9 * b3
        if round(b6, 2) == 0:
            return round(b5, 2)
        elif b6 > 0:
            b7 = b5
        else:
            b8 = b5
    return round(b5, 2)
def fonk3():
    b4 = 100000
    a1 = 12
    a2 = 0.22
    a3 = 0.05
    b9 = a2 / 12.0
    new_balance, b1 = fonk1(b4, a3, b9, a1)
    b10 = round(sum(b1) / len(b1), 2)
    b11 = round(abs(b4 - new_balance - sum(b1)), 2)
    b12 = b4 / 12
    b13 = (b4 * (1 + b9) ** a1) / a1
    b14 = fonk2(b4, b9, a1, b12, b13)
    b15 = round(abs(b4 - 0 - b14 * a1), 2)
    print('Current Balance:', b4, '')
    print('Duration:', a1, 'a1')
    print(f'With a monthly b14 rate of {a3:.2f}:')
    print(f'   - You will pay {b10}  per month on average.')
    print(f'   - Your loss will be {b11}  for that time period.')
    print(f'   - Your remaining b4 will be {new_balance} .')
    print(f'If you want to pay off your b4 within {a1} a1:')
    print(f'   - You will have to pay {b14}  per month.')
    print(f'   - Your loss will be {b15}  in total.')
    print('   - Your remaining b4 will be 0 .')
if b16 = = "__main__":
    fonk3()