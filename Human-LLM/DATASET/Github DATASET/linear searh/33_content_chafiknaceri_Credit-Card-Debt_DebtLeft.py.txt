def CalculateYearlyBalance(balance,annualIntrest,MonthlyRate):
    """
        this function takes in : balance , annual interest,monthly rate
        returns the debt left at the end of the year
    """
    unPaidBalance = balance
    for i in range(12):
        unPaidBalance = unPaidBalance - (MonthlyRate *  unPaidBalance)
        intrestAmount = (annualIntrest/12) * unPaidBalance
        unPaidBalance +=intrestAmount
    return unPaidBalance
