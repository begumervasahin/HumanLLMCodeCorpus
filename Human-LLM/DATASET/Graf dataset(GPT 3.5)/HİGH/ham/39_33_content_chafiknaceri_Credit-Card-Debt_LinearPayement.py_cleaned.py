def fonk1(balance,annualIntrest):
    b1 = balance
    a1 = 0
    while b1 >= 0 :
        b1 = balance
        for i in range(12):
            b1 = b1 - a1
            b2 = (annualIntrest/12) * b1
            b1 +=b2
        a1+=10
    return a1 -10