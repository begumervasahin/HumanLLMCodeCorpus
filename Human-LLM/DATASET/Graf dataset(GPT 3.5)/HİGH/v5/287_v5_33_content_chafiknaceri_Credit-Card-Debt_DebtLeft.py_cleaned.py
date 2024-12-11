def fonk1(initial_balance, annual_interest_rate, monthly_payment_rate):
    b1 = initial_balance
    for _ in range(12):
        b1 -= monthly_payment_rate * b1
        b2 = (annual_interest_rate / 12) * b1
        b1 += b2
    return b1