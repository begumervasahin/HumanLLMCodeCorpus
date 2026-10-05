def calculate_yearly_balance(initial_balance, annual_interest_rate, monthly_payment_rate):
    remaining_balance = initial_balance
    for _ in range(12):
        remaining_balance -= monthly_payment_rate * remaining_balance
        interest_amount = (annual_interest_rate / 12) * remaining_balance
        remaining_balance += interest_amount
    return remaining_balance