def CalculateYearlyBalance(balance,annualIntrest):
    unPaidBalance = balance
    MonthlyRate = 0
    while unPaidBalance >= 0 :
        unPaidBalance = balance
        for i in range(12):
            unPaidBalance = unPaidBalance - MonthlyRate
            intrestAmount = (annualIntrest/12) * unPaidBalance
            unPaidBalance +=intrestAmount
        MonthlyRate+=10
    return MonthlyRate -10