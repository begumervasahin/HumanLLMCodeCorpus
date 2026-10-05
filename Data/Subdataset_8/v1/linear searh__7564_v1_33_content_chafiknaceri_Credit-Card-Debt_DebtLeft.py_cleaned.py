def CalculateYearlyBalance(balance, annualInterest, monthlyRate):
    unpaidBalance = balance
    for i in range(12):
        unpaidBalance = unpaidBalance - (monthlyRate * unpaidBalance)
        interestAmount = (annualInterest / 12) * unpaidBalance
        unpaidBalance += interestAmount
    return unpaidBalance
initialBalance = float(input("Enter the initial balance: "))
annualInterestRate = float(input("Enter the annual interest rate (as a decimal): "))
monthlyInterestRate = float(input("Enter the monthly interest rate (as a decimal): "))
finalDebt = CalculateYearlyBalance(initialBalance, annualInterestRate, monthlyInterestRate)
print(f"The remaining debt at the end of the year is: {finalDebt:.2f}")