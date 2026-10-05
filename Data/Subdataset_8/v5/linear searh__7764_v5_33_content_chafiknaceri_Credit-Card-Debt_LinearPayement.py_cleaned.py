def calculate_yearly_balance(initial_balance, annual_interest_rate):
    remaining_balance = initial_balance
    monthly_payment = 0
    while remaining_balance >= 0:
        remaining_balance = initial_balance
        for _ in range(12):
            remaining_balance -= monthly_payment
            monthly_interest = (annual_interest_rate / 12) * remaining_balance
            remaining_balance += monthly_interest
        monthly_payment += 10
    return monthly_payment - 10