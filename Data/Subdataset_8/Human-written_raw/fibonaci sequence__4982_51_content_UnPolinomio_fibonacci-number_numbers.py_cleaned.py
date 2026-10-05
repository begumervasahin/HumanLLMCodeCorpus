quantity = input("\nHow many numbers do you want to calculate?\n>> ")
def calculate_numbers(howMany):
    sequence = [1, 1]
    for i in range(howMany-2):
        actualIndex = i + 2
        sequence.append(sequence[actualIndex-1] + sequence[actualIndex-2])
    for i,num in enumerate(sequence):
        print(str(i+1) + ".-", num)
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