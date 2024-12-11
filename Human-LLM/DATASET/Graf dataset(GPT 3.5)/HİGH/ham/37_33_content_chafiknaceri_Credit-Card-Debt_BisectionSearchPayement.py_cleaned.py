def fonk1(balance,annualIntrest):
    b1 = balance
    b2 = annualIntrest / 12
    b3 = b1 / 12
    b4 = (b1 * ((1+ b2)**12) ) / 12
    while abs(b1) > 0.01    :
        b5 = (b3 + b4) / 2
        b1 = balance
        for i in range(12):
            b1 = b1 - b5
            b6 = (annualIntrest/12) * b1
            b1 +=b6
        if(b1 > 0.01):
            b3 = b5
        elif b1 < -0.01:
            b4 = b5
        else:
            break
            b4 = b5
    return round(b5,2)