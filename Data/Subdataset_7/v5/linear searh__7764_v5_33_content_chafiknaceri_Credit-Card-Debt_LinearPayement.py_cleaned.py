def fonk1(initial_balance, annual_interest_rate):
    b1 = initial_balance
    a1 = 0
    while b1 >= 0:
        b1 = initial_balance
        for _ in range(12):
            b1 -= a1
            b2 = (annual_interest_rate / 12) * b1
            b1 += b2
        a1 += 10
    return a1 - 10