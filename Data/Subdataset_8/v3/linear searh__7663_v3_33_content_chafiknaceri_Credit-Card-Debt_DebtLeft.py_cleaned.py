def calculate_yearly_balance(initial_balance, annual_interest, monthly_rate):
    unpaid_balance = initial_balance
    for _ in range(12):
        unpaid_balance -= monthly_rate * unpaid_balance
        monthly_interest = (annual_interest / 12)
        interest_amount = monthly_interest * unpaid_balance
        unpaid_balance += interest_amount
    return unpaid_balance
initial_balance = float(input("Enter the initial balance: "))
annual_interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
monthly_interest_rate = float(input("Enter the monthly interest rate (as a decimal): "))
final_debt = calculate_yearly_balance(initial_balance, annual_interest_rate, monthly_interest_rate)
print(f"The remaining debt at the end of the year is: {final_debt:.2f}")