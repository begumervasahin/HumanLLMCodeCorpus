def fonk1(b3, a3, b5, a1, b6):
    if a1 <= 0:
        return round(b3, 2), b6
    else:
        b1 = a3 * b3
        b6.append(b1)
        b2 = b3 - b1
        b3 = b2 + b5 * b2
        return fonk1(b3, a3, b5, a1 - 1, b6)
def fonk2(b3, b5, a1, lower, upper):
    b4 = (lower + upper) / 2
    if a1 <= 0:
        if round(b3) == 0:
            return round(b4, 2)
        elif b3 < 0:
            return fonk2(b3, b5, a1, lower, b4)
        else:
            return fonk2(b3, b5, a1, b4, upper)
    else:
        b2 = b3 - b4
        b3 = b2 + b5 * b2
        return fonk2(b3, b5, a1 - 1, lower, upper)
def fonk3():
    b3 = 100000
    a1 = 12
    a2 = 0.22
    a3 = 0.05
    b5 = a2 / 12.0
    b6 = []
    new_balance, b6 = fonk1(b3, a3, b5, a1, b6)
    b7 = round(sum(b6) / len(b6), 2)
    b8 = round(abs(b3 - new_balance - sum(b6)), 2)
    b9 = b3 / 12
    b10 = (b3 * (1 + b5) ** a1) / a1
    b11 = fonk2(b3, b5, a1, b9, b10)
    b12 = round(abs(b3 - 0 - b11 * a1), 2)
    print('Current Balance:', b3, '')
    print('Duration:', a1, 'a1')
    print('With a monthly b11 rate of {:.2f}:'.format(a3))
    print('   - You will pay', b7, ' per month on average.')
    print('   - Your loss will be', b8, ' for that time period.')
    print('   - Your remaining b3 will be', new_balance, '.')
    print('If you want to pay off your b3 within', a1, 'a1:')
    print('   - You will have to pay', b11, ' per month.')
    print('   - Your loss will be', b12, ' in total.')
    print('   - Your remaining b3 will be 0 .')
if b13 = = "__main__":
    fonk3()