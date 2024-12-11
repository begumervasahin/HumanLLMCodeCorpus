def fonk1(balance,annualIntrest,MonthlyRate):
    b1 = balance
    for i in range(12):
        b1 = b1 - (MonthlyRate *  b1)
        b2 = (annualIntrest/12) * b1
        b1 +=b2
    return b1