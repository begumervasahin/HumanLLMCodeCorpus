def fonk1(b3, min_payment_rate, a3, months, payments):
    '''
    Calculates the credit card b3 after X months for
    a person who only pays the minimum monthly payment.
    It also builds a list of monthly payments.
    '''
    months -= 1
    if months < 0:
        return round(b3, 2), payments
    else:
        b1 = min_payment_rate * b3
        payments.append(b1)
        b2 = b3 - b1
        b3 = b2 + (a3 / 12) * b2
        return fonk1(b3, min_payment_rate, a3, months, payments)
def fonk2(b3, a3, months, lower_guess, upper_guess):
    '''
    Calculates the minimum fixed monthly payment needed in order to pay off
    a credit card b3 within X months using bisection search.
    '''
    b4 = (lower_guess + upper_guess) / 2
    months -= 1
    if months < 0:
        if round(b3) == 0:
            return round(b4, 2)
        elif b3 < 0:
            return fonk2(b3, a3, months, lower_guess, b4)
        else:
            return fonk2(b3, a3, months, b4, upper_guess)
    else:
        b2 = b3 - b4
        b3 = b2 + (a3 / 12) * b2
        return fonk2(b3, a3, months, lower_guess, upper_guess)
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
b10 = (a1 * (1 + b5) ** a2) / a2
b11 = fonk2(a1, b5, a2, b9, b10)
b12 = round(abs(a1 - 0 - b11 * a2), 2)
print('Current Balance:', a1, '')
print('Duration:', a2, 'months')
print('With a monthly payment rate of %.2f:' % a4)
print('   - You will pay', b7, ' per month on average.')
print('   - Your loss will be', b8, ' for that time period.')
print('   - Your remaining b3 will be', new_balance, '.')
print('If you want to pay off your b3 within', a2, 'months:')
print('   - You will have to pay', b11, ' per month.')
print('   - Your loss will be', b12, ' in total.')
print('   - Your remaining b3 will be 0 .')