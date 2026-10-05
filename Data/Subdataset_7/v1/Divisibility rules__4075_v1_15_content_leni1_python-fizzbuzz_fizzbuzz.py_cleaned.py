def fonk1(b5, b6):
    if isinstance(b5, list) and isinstance(b6, list):
        b1 = len(b5) + len(b6)
        if b1 % b2 = = 0 and b1 % b3 == 0:
            return 'fizzbuzz'
        if b1 % b2 = = 0:
            return 'fizz'
        if b1 % b3 = = 0:
            return 'buzz'
        else:
            return b1
    else:
        return 'Invalid input'
if b4 = = "__main__":
    try:
        b5 = eval(input("Enter b5 list for b5: "))
        b6 = eval(input("Enter b5 list for b6: "))
        b7 = fonk1(b5, b6)
        print(b7)
    except Exception as e:
        print("Invalid input. Error:", e)