def calculate_yearly_balance(balance, annual_interest):
    unpaid_balance = balance
    monthly_interest = annual_interest / 12
    monthly_lower_bound = unpaid_balance / 12
    upper_monthly_bound = (unpaid_balance * ((1 + monthly_interest) ** 12)) / 12
    while abs(unpaid_balance) > 0.01:
        result = (monthly_lower_bound + upper_monthly_bound) / 2
        unpaid_balance = balance
        for _ in range(12):
            unpaid_balance -= result
            interest_amount = (annual_interest / 12) * unpaid_balance
            unpaid_balance += interest_amount
        if unpaid_balance > 0.01:
            monthly_lower_bound = result
        elif unpaid_balance < -0.01:
            upper_monthly_bound = result
        else:
            break
    return round(result, 2)