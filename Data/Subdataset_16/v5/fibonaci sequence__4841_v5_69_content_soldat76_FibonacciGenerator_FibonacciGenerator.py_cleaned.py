def fonk1(b1):
    if b1 <= 0:
        return "The sequence must contain some positive number."
    elif b1 = = 1:
        return [1]
    elif b1 = = 2:
        return [1, 1]
    b2 = [1, 1]
    while len(b2) < b1:
        b3 = b2[-2] + b2[-1]
        b2.append(b3)
    return b2
def fonk2(b1, b2):
    print(f"\nHere is your Fibonacci sequence of {b1} number(s):\n\t{b2}")
def fonk3():
    print("\nThis program will print out a Fibonacci sequence of your desired b1!")
    while True:
        try:
            b1 = int(input("\nEnter your desired Fibonacci sequence b1: "))
            if b1 <= 0:
                print("The sequence must contain some positive number.")
                continue
            b2 = fonk1(b1)
            if isinstance(b2, str):
                print(b2)
            else:
                fonk2(b1, b2)
        except ValueError:
            print("Please enter a valid number.")
        b4 = input("\nDo you want to generate another sequence? (yes/no): ").strip().lower()
        if b4 != 'yes':
            break
if b5 = = "__main__":
    fonk3()