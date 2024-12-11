def fonk1(b4, annual_interest, monthly_rate):
    b1 = b4
    for _ in range(12):
        b1 -= monthly_rate * b1
        b2 = (annual_interest / 12)
        b3 = b2 * b1
        b1 += b3
    return b1
b4 = float(input("Enter the initial balance: "))
b5 = float(input("Enter the annual interest rate (as a decimal): "))
b6 = float(input("Enter the monthly interest rate (as a decimal): "))
b7 = fonk1(b4, b5, b6)
print(f"The remaining debt at the end of the year is: {b7:.2f}")