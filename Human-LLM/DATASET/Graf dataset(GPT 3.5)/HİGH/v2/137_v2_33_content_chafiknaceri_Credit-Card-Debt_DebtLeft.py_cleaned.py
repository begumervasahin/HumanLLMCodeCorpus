def fonk1(b3, annual_interest, monthly_rate):
    b1 = b3
    for month in range(12):
        b1 -= monthly_rate * b1
        b2 = (annual_interest / 12) * b1
        b1 += b2
    return b1
b3 = float(input("Enter the initial balance: "))
b4 = float(input("Enter the annual interest rate (as a decimal): "))
b5 = float(input("Enter the monthly interest rate (as a decimal): "))
b6 = fonk1(b3, b4, b5)
print(f"The remaining debt at the end of the year is: {b6:.2f}")