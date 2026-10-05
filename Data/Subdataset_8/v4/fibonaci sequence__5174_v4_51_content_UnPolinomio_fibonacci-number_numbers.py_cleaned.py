def calculate_fibonacci_sequence(length):
    sequence = [1, 1]
    for i in range(length - 2):
        actual_index = i + 2
        sequence.append(sequence[actual_index - 1] + sequence[actual_index - 2])
    for index, number in enumerate(sequence):
        print(f"{index + 1}.- {number}")
quantity = input("\nHow many Fibonacci numbers do you want to calculate?\n>> ")
if quantity == "":
    print("\nError: Please insert a value.")
else:
    try:
        quantity = int(quantity)
    except ValueError:
        print("\nError: Please insert an integer number.")
    else:
        if quantity < 2:
            print("\nError: Please insert a positive number greater than or equal to 2.")
        else:
            calculate_fibonacci_sequence(quantity)