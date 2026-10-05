def calculate_yearly_balance(balance, annual_interest):
    unpaid_balance = balance
    monthly_rate = 0
    while unpaid_balance >= 0:
        unpaid_balance = balance
        for _ in range(12):
            unpaid_balance -= monthly_rate
            interest_amount = (annual_interest / 12) * unpaid_balance
            unpaid_balance += interest_amount
        monthly_rate += 10
    return monthly_rate - 10
balance_input = float(input("Enter Yearly Debt: "))
interest_input = float(input("Enter Annual Interest Rate (as a decimal): "))
result = calculate_yearly_balance(balance_input, interest_input)
print(f"The minimum monthly payment to pay off all debt in a year is: ${result}")