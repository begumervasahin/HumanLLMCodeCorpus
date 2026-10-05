def calculate_numbers(how_many):
    sequence = [1, 1]
    for i in range(how_many - 2):
        actual_index = i + 2
        sequence.append(sequence[actual_index - 1] + sequence[actual_index - 2])
    for i, num in enumerate(sequence):
        print(f"{i + 1}.- {num}")
quantity = input("\nHow many numbers do you want to calculate?\n>> ")
if quantity == "":
    print("\nError: Please insert a value.")
else:
    try:
        quantity = int(quantity)
    except ValueError:
        print("\nError: Insert an integer number please.")
    else:
        if quantity < 2:
            print("\nError: Please insert a positive number; where number >= 2.")
        else:
            calculate_numbers(quantity)