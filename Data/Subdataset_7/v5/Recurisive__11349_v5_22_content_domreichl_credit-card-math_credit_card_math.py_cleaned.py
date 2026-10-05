def fonk1(b4, min_payment_rate, a3, months, payments):
    '''
    Calculates the credit card b4 after X months for
    a person who only pays the minimum monthly payment.
    It also builds a list of monthly payments.
    '''
    months -= 1
    if months < 0:
        return round(b4, 2), payments
    else:
        b1 = min_payment_rate * b4
        payments.append(b1)
        b2 = b4 - b1
        b3 = (a3 / 12) * b2
        b4 = b2 + b3
        return fonk1(b4, min_payment_rate, a3, months, payments)
def fonk2(b4, a3, months, lower_guess, upper_guess):
    '''
    Calculates the minimum fixed monthly payment needed in order to pay off
    a credit card b4 within X months using bisection search.
    '''
    b5 = (lower_guess + upper_guess) / 2
    months -= 1
    if months < 0:
        if round(b4) == 0:
            return round(b5, 2)
        elif b4 < 0:
            return fonk2(b4, a3, months, lower_guess, b5)
        else:
            return fonk2(b4, a3, months, b5, upper_guess)
    else:
        b2 = b4 - b5
        b3 = (a3 / 12) * b2
        b4 = b2 + b3
        return fonk2(b4, a3, months, lower_guess, upper_guess)
a1 = 100000
a2 = 12
a3 = 0.22
a4 = 0.05
b6 = a3 / 12
b7 = []
new_balance, b7 = fonk1(a1, a4, b6, a2, b7)
b8 = round(sum(b7) / len(b7), 2)
b9 = round(abs(a1 - new_balance - sum(b7)), 2)
b10 = a1 / 12
b11 = (a1 * (1 + b6) ** a2) / a2
b12 = fonk2(a1, b6, a2, b10, b11)
b13 = round(abs(a1 - 0 - b12 * a2), 2)
print('Current Balance:', a1, '')
print('Duration:', a2, 'months')
print('With a monthly payment rate of %.2f:' % a4)
print('   - You will pay', b8, ' per month on average.')
print('   - Your loss will be', b9, ' for that time period.')
print('   - Your remaining b4 will be', new_balance, '.')
print('If you want to pay off your b4 within', a2, 'months:')
print('   - You will have to pay', b12, ' per month.')
print('   - Your loss will be', b13, ' in total.')
print('   - Your remaining b4 will be 0 .')