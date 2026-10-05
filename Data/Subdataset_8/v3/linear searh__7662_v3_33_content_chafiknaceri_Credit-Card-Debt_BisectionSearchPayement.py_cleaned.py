def calculate_yearly_balance(balance, annual_interest):
    unpaid_balance = balance
    monthly_interest = annual_interest / 12
    lower_bound = unpaid_balance / 12
    upper_bound = (unpaid_balance * ((1 + monthly_interest) ** 12)) / 12
    while abs(unpaid_balance) > 0.01:
        payment_guess = (lower_bound + upper_bound) / 2
        unpaid_balance = balance
        for _ in range(12):
            unpaid_balance -= payment_guess
            interest_amount = (annual_interest / 12) * unpaid_balance
            unpaid_balance += interest_amount
        if unpaid_balance > 0.01:
            lower_bound = payment_guess
        elif unpaid_balance < -0.01:
            upper_bound = payment_guess
        else:
            break
    return round(payment_guess, 2)
balance = 5000
annual_interest = 0.18
monthly_payment = calculate_yearly_balance(balance, annual_interest)
print("Monthly Payment:", monthly_payment)