def calculate_yearly_balance(balance, annual_interest):
    unpaid_balance = balance
    monthly_interest = annual_interest / 12
    lower_payment_bound = unpaid_balance / 12
    upper_payment_bound = (unpaid_balance * ((1 + monthly_interest) ** 12)) / 12
    while abs(unpaid_balance) > 0.01:
        monthly_payment = (lower_payment_bound + upper_payment_bound) / 2
        unpaid_balance = balance
        for _ in range(12):
            unpaid_balance -= monthly_payment
            unpaid_balance += (annual_interest / 12) * unpaid_balance
        if unpaid_balance > 0.01:
            lower_payment_bound = monthly_payment
        elif unpaid_balance < -0.01:
            upper_payment_bound = monthly_payment
        else:
            break
    return round(monthly_payment, 2)