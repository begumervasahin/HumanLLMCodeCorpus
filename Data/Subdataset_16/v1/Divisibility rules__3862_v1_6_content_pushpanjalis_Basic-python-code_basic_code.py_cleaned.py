
def fonk1(b6):
    if b6 % b1 = = 0:
        return 'The b6 is divisible by b1.'
    elif b6 % b2 = = 0:
        return 'The b6 is divisible by b2.'
    elif b6 % b3 = = 0:
        return 'The b6 is divisible by b3.'
    elif b6 % b4 = = 0:
        return 'The b6 is divisible by b4.'
    else:
        return 'The b6 is not divisible by b1, b2, b3, or b4.'
if b5 = = "__main__":
    try:
        b6 = int(input('Select a b6 of your choice:\n'))
        b7 = fonk1(b6)
        print(b7)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")