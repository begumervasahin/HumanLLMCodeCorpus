def CalculateYearlyBalance(balance,annualIntrest,MonthlyRate):
    unPaidBalance = balance
    for i in range(12):
        unPaidBalance = unPaidBalance - (MonthlyRate *  unPaidBalance)
        intrestAmount = (annualIntrest/12) * unPaidBalance
        unPaidBalance +=intrestAmount
    return unPaidBalance