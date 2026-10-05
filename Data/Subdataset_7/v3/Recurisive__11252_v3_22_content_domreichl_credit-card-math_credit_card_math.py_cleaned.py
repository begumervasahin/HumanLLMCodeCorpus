def fonk1(b3, min_payment_rate, a3, a2, b6):
    '''
    Calculates the credit card b3 after X a2 for
    a person who only pays the minimum monthly b11.
    It also builds a list of monthly b6.
    '''
    a2 -= 1
    if a2 < 0:
        return round(b3, 2), b6
    else:
        b1 = min_payment_rate * b3
        b6.append(b1)
        b2 = b3 - b1
        b3 = b2 + (a3 / 12) * b2
        return fonk1(b3, min_payment_rate, a3, a2, b6)
def fonk2(b3, a3, a2, lower_guess, upper_guess):
    '''
    Calculates the minimum fixed monthly b11 needed to pay off
    a credit card b3 within X a2 using bisection search.
    '''
    b4 = (lower_guess + upper_guess) / 2
    a2 -= 1
    if a2 < 0:
        if round(b3) == 0:
            return round(b4, 2)
        elif b3 < 0:
            return fonk2(b3, a3, a2, lower_guess, b4)
        else:
            return fonk2(b3, a3, a2, b4, upper_guess)
    else:
        b2 = b3 - b4
        b3 = b2 + (a3 / 12) * b2
        return fonk2(b3, a3, a2, lower_guess, upper_guess)
def fonk3():
    a1 = 100000
    a2 = 12
    a3 = 0.22
    a4 = 0.05
    b5 = a3 / 12
    b6 = []
    new_balance, b6 = fonk1(a1, a4, b5, a2, b6)
    b7 = round(sum(b6) / len(b6), 2)
    b8 = round(abs(a1 - new_balance - sum(b6)), 2)
    b9 = a1 / 12
    b10 = (a1 * (1 + b5)**a2) / a2
    b11 = fonk2(a1, a3, a2, b9, b10)
    b12 = round(abs(a1 - 0 - b11 * a2), 2)
    print('Current Balance:', a1, '')
    print('Duration:', a2, 'a2')
    print('With a monthly b11 rate of %.2f:' % a4)
    print('   - You will pay', b7, ' per month on average.')
    print('   - Your loss will be', b8, ' for that time period.')
    print('   - Your remaining b3 will be', new_balance, '.')
    print('If you want to pay off your b3 within', a2, 'a2:')
    print('   - You will have to pay', b11, ' per month.')
    print('   - Your loss will be', b12, ' in total.')
    print('   - Your remaining b3 will be 0 .')
if b13 = = '__main__':
    fonk3()