def fonk1(balance, annual_interest, monthly_rate):
    b1 = balance
    for _ in range(12):
        b1 -= monthly_rate * b1
        b2 = (annual_interest / 12) * b1
        b1 += b2
    return b1