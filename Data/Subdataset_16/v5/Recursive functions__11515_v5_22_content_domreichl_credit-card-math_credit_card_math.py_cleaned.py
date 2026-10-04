def fonk1(b4, a3, b10, a1):
    b1 = []
    for _ in range(a1):
        b2 = a3 * b4
        b1.append(b2)
        b3 = b4 - b2
        b4 = b3 + b10 * b3
    return round(b4, 2), b1
def fonk2(b4, b10, a1, b8, b7):
    while a1 > 0:
        b5 = (b8 + b7) / 2
        b6 = b4
        for _ in range(a1):
            b3 = b6 - b5
            b6 = b3 + b10 * b3
        if round(b6, 2) == 0:
            return round(b5, 2)
        elif b6 < 0:
            b7 = b5
        else:
            b8 = b5
    return round(b5, 2)
if b9 = = "__main__":
    b4 = 100000
    a1 = 12
    a2 = 0.22
    a3 = 0.05
    b10 = a2 / 12
    new_balance, b1 = fonk1(b4, a3, b10, a1)
    b11 = round(sum(b1) / len(b1), 2)
    b12 = round(abs(b4 - new_balance - sum(b1)), 2)
    b13 = b4 / 12
    b14 = (b4 * (1 + b10) ** a1) / a1
    b15 = fonk2(b4, b10, a1, b13, b14)
    b16 = round(abs(b4 - b15 * a1), 2)
    print(f"Current Balance: {b4} ")
    print(f"Duration: {a1} a1")
    print(f"With a monthly b15 rate of {a3:.2f}:")
    print(f"   - You will pay {b11}  per month on average.")
    print(f"   - Your loss will be {b12}  for that time period.")
    print(f"   - Your remaining b4 will be {new_balance} .")
    print(f"If you want to pay off your b4 within {a1} a1:")
    print(f"   - You will have to pay {b15}  per month.")
    print(f"   - Your loss will be {b16}  in total.")
    print(f"   - Your remaining b4 will be 0 .")