def calculate_fibonacci_sequence(length):
    fibonacci_sequence = [1, 1]
    for i in range(2, length):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    for index, number in enumerate(fibonacci_sequence, 1):
        print(f"{index}. {number}")
quantity_input = input("\nHow many Fibonacci numbers do you want to calculate?\n>> ")
if quantity_input.strip() == "":
    print("\nError: Please insert a value.")
else:
    try:
        quantity = int(quantity_input)
        if quantity < 2:
            raise ValueError("Quantity must be greater than or equal to 2.")
    except ValueError:
        print("\nError: Please insert an integer greater than or equal to 2.")
    else:
        calculate_fibonacci_sequence(quantity)