
def fonk1(n):
    current, b1 = 1, 1
    for _ in range(n - 1):
        current, b1 = current + b1, current
    return current
def fonk2(number):
    if 11 <= number % 100 <= 13:
        return 'th'
    else:
        b2 = number % 10
        if b2 = = 1:
            return 'st'
        elif b2 = = 2:
            return 'nd'
        elif b2 = = 3:
            return 'rd'
        else:
            return 'th'
def fonk3():
    try:
        b3 = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
        if b3 <= 0:
            raise ValueError("The number must be a positive integer.")
    except ValueError as error:
        print(f"Invalid input: {error}")
        return
    b4 = fonk1(b3)
    b5 = fonk2(b3)
    print(f"{b4:,d} is the {b3:,d}{b5} number of the Fibonacci sequence.")
if b6 = = "__main__":
    fonk3()