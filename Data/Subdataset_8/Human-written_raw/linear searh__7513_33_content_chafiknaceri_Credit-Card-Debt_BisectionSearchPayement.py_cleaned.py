def CalculateYearlyBalance(balance,annualIntrest):
    unPaidBalance = balance
    monthlyIntrest = annualIntrest / 12
    monthlyLowerBond = unPaidBalance / 12
    upperMonthlyBond  = (unPaidBalance * ((1+ monthlyIntrest)**12) ) / 12
    while abs(unPaidBalance) > 0.01    :
        result = (monthlyLowerBond + upperMonthlyBond) / 2
        unPaidBalance = balance
        for i in range(12):
            unPaidBalance = unPaidBalance - result
            intrestAmount = (annualIntrest/12) * unPaidBalance
            unPaidBalance +=intrestAmount
        if(unPaidBalance > 0.01):
            monthlyLowerBond = result
        elif unPaidBalance < -0.01:
            upperMonthlyBond = result
        else:
            break
            upperMonthlyBond = result
    return round(result,2)