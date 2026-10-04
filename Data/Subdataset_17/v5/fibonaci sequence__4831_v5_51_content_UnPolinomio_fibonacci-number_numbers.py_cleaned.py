def calculate_numbers(how_many):
    sequence = [1, 1]
    for i in range(2, how_many):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    for index, number in enumerate(sequence):
        print(f"{index + 1}.- {number}")
def main():
    quantity = input("\nHow many numbers do you want to calculate?\n>> ")
    if not quantity:
        print("\nError: Please insert a value.")
        return
    try:
        quantity = int(quantity)
    except ValueError:
        print("\nError: Insert an integer number please.")
        return
    if quantity < 2:
        print("\nError: Please insert a positive number; where number >= 2.")
    else:
        calculate_numbers(quantity)
if __name__ == "__main__":
    main()