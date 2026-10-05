def generate_fibonacci_sequence(limit):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < limit:
        current = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(current)
    return fibonacci_sequence[:limit]
while True:
    try:
        num_fibonacci = int(input("How many Fibonacci numbers do you want to generate? "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue
    if num_fibonacci <= 0:
        print("Please enter a positive integer.")
        continue
    fibonacci_numbers = generate_fibonacci_sequence(num_fibonacci)
    print(f"Fibonacci sequence: {fibonacci_numbers}")
    break