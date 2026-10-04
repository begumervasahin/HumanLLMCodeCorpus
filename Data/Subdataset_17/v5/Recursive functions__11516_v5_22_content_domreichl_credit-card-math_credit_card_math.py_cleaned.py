def calc_balance(balance, min_payment_rate, monthly_interest_rate, months):
    payments = []
    for _ in range(months):
        min_payment = min_payment_rate * balance
        payments.append(min_payment)
        unpaid_balance = balance - min_payment
        balance = unpaid_balance + monthly_interest_rate * unpaid_balance
    return round(balance, 2), payments
def pay_off_debt(balance, monthly_interest_rate, months, lower, upper):
    while months > 0:
        guess = (lower + upper) / 2
        temp_balance = balance
        for _ in range(months):
            unpaid_balance = temp_balance - guess
            temp_balance = unpaid_balance + monthly_interest_rate * unpaid_balance
        if round(temp_balance, 2) == 0:
            return round(guess, 2)
        elif temp_balance < 0:
            upper = guess
        else:
            lower = guess
    return round(guess, 2)
if __name__ == "__main__":
    balance = 100000
    months = 12
    annual_interest_rate = 0.22
    min_payment_rate = 0.05
    monthly_interest_rate = annual_interest_rate / 12
    new_balance, payments = calc_balance(balance, min_payment_rate, monthly_interest_rate, months)
    average_payment = round(sum(payments) / len(payments), 2)
    loss1 = round(abs(balance - new_balance - sum(payments)), 2)
    min_guess = balance / 12
    max_guess = (balance * (1 + monthly_interest_rate) ** months) / months
    payment = pay_off_debt(balance, monthly_interest_rate, months, min_guess, max_guess)
    loss2 = round(abs(balance - payment * months), 2)
    print(f"Current Balance: {balance} ")
    print(f"Duration: {months} months")
    print(f"With a monthly payment rate of {min_payment_rate:.2f}:")
    print(f"   - You will pay {average_payment}  per month on average.")
    print(f"   - Your loss will be {loss1}  for that time period.")
    print(f"   - Your remaining balance will be {new_balance} .")
    print(f"If you want to pay off your balance within {months} months:")
    print(f"   - You will have to pay {payment}  per month.")
    print(f"   - Your loss will be {loss2}  in total.")
    print(f"   - Your remaining balance will be 0 .")