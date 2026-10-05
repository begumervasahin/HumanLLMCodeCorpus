def fonk1(balance, annual_interest):
    b1 = balance
    a1 = 0
    while b1 >= 0:
        b1 = balance
        for _ in range(12):
            b1 -= a1
            b2 = (annual_interest / 12) * b1
            b1 += b2
        a1 += 10
    return a1 - 10
b3 = float(input("Enter the total debt for the year: "))
b4 = float(input("Enter the annual interest rate (as a decimal): "))
b5 = fonk1(b3, b4)
print(f"The minimum monthly payment required to pay off the debt in a year is: ${b5}")