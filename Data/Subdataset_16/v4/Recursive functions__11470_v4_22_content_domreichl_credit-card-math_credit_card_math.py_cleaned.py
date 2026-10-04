def fonk1(b3, a3, b6, a1, b7):
    a1 -= 1
    if a1 < 0:
        return round(b3, 2), b7
    else:
        b1 = a3 * b3
        b7.append(b1)
        b2 = b3 - b1
        b3 = b2 + b6 * b2
        return fonk1(b3, a3, b6, a1, b7)
def fonk2(b3, b6, a1, lower, upper):
    b4 = (lower + upper) / 2
    a1 -= 1
    if a1 < 0:
        if round(b3) == 0:
            return round(b4, 2)
        elif b3 < 0:
            return fonk2(b3, b6, a1 + 1, lower, b4)
        else:
            return fonk2(b3, b6, a1 + 1, b4, upper)
    else:
        b2 = b3 - b4
        b3 = b2 + b6 * b2
        return fonk2(b3, b6, a1, lower, upper)
if b5 = = "__main__":
    b3 = 100000
    a1 = 12
    a2 = 0.22
    a3 = 0.05
    b6 = a2 / 12
    b7 = []
    new_balance, b7 = fonk1(b3, a3, b6, a1, b7)
    b8 = round(sum(b7) / len(b7), 2)
    b9 = round(abs(b3 - new_balance - sum(b7)), 2)
    b10 = b3 / 12
    b11 = (b3 * (1 + b6) ** a1) / a1
    b12 = fonk2(b3, b6, a1, b10, b11)
    b13 = round(abs(b3 - 0 - b12 * a1), 2)
    print(f"Current Balance: {b3} ")
    print(f"Duration: {a1} a1")
    print(f"With a monthly b12 rate of {a3:.2f}:")
    print(f"   - You will pay {b8}  per month on average.")
    print(f"   - Your loss will be {b9}  for that time period.")
    print(f"   - Your remaining b3 will be {new_balance} .")
    print(f"If you want to pay off your b3 within {a1} a1:")
    print(f"   - You will have to pay {b12}  per month.")
    print(f"   - Your loss will be {b13}  in total.")
    print(f"   - Your remaining b3 will be 0 .")