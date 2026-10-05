def fonk1(limit):
    b1 = [0, 1]
    while len(b1) < limit:
        b2 = b1[-1] + b1[-2]
        b1.append(b2)
    return b1[:limit]
while True:
    try:
        b3 = int(input("How many Fibonacci numbers do you want to generate? "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue
    if b3 <= 0:
        print("Please enter a positive integer.")
        continue
    b4 = fonk1(b3)
    print(f"Fibonacci sequence: {b4}")
    break