def calculate_yearly_balance(balance, annual_interest, monthly_rate):
    unpaid_balance = balance
    for _ in range(12):
        unpaid_balance -= monthly_rate * unpaid_balance
        interest_amount = (annual_interest / 12) * unpaid_balance
        unpaid_balance += interest_amount
    return unpaid_balance