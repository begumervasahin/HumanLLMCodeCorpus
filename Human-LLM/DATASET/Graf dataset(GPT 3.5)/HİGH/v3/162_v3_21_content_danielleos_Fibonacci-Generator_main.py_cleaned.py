def fonk1(limit):
    b1 = [0, 1]
    while len(b1) < limit:
        b1.append(b1[-1] + b1[-2])
    return b1[:limit]
while True:
    try:
        b2 = int(input("How many Fibonacci numbers do you want to generate? "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue
    if b2 <= 0:
        print("Please enter a positive integer.")
        continue
    else:
        print(f"Generating {b2} Fibonacci numbers...")
        b3 = fonk1(b2)
        print(f"Fibonacci sequence: {b3}")
        break