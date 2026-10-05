def generate_fibonacci_sequence(limit):
    fibonacci_sequence = []
    current = 0
    previous1 = 0
    previous2 = 0
    for i in range(1, limit):
        if i == 1:
            fibonacci_sequence.append(current)
            current += 1
            fibonacci_sequence.append(current)
            previous2 = previous1
            previous1 = current
        else:
            current = previous2 + previous1
            fibonacci_sequence.append(current)
            previous2 = previous1
            previous1 = current
    return fibonacci_sequence
while True:
    try:
        num_fibonacci = int(input("How many Fibonacci numbers do you want to generate? "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue
    if num_fibonacci <= 0:
        print("Please enter a positive integer.")
        continue
    else:
        print(f"Generating {num_fibonacci} Fibonacci numbers...")
        fibonacci_numbers = generate_fibonacci_sequence(num_fibonacci)
        print(f"Fibonacci sequence: {fibonacci_numbers}")
        break