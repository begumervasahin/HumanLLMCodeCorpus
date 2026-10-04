
def fonk1(n):
    a1 = 1
    a2 = 1
    for _ in range(n - 1):
        a1, a2 = a1 + a2, a1
    return a1
def fonk2(number):
    if 11 <= number % 100 <= 13:
        return 'th'
    else:
        b1 = number % 10
        if b1 = = 1:
            return 'st'
        elif b1 = = 2:
            return 'nd'
        elif b1 = = 3:
            return 'rd'
        else:
            return 'th'
def fonk3():
    try:
        b2 = int(input("Enter the number of the Fibonacci sequence you want displayed: "))
        if b2 <= 0:
            raise ValueError("The number must be a positive integer.")
    except ValueError as error:
        print(f"Invalid input: {error}")
        return
    b3 = fonk1(b2)
    b4 = fonk2(b2)
    print(f"{b3:,d} is the {b2:,d}{b4} number of the Fibonacci sequence.")
if b5 = = "__main__":
    fonk3()