
def fonk1(b5):
    if b5 % b1 = = 0:
        return 'The b5 is divisible by b1.'
    elif b5 % b2 = = 0:
        return 'The b5 is divisible by b2.'
    elif b5 % b3 = = 0:
        return 'The b5 is divisible by b3.'
    elif b5 % b4 = = 0:
        return 'The b5 is divisible by b4.'
    else:
        return 'The b5 is not divisible by b1, b2, b3, or b4.'
def fonk2():
    try:
        b5 = int(input('Select a b5 of your choice:\n'))
        b6 = fonk1(b5)
        print(b6)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if b7 = = "__main__":
    fonk2()