def fonk1(b1, sequence):
    print(f"\nHere is your Fibonacci sequence of {b1} number(s):")
    print("\t", sequence)
def fonk2(b1):
    if b1 <= 0:
        print("The sequence must contain at least one positive number.")
        return None
    elif b1 = = 1:
        return [1]
    elif b1 = = 2:
        return [1, 1]
    else:
        b2 = [1, 1]
        for _ in range(2, b1):
            b3 = b2[-1] + b2[-2]
            b2.append(b3)
        return b2
if b4 = = "__main__":
    print("\nThis program will print out a Fibonacci sequence of your desired b1!")
    while True:
        b1 = int(input("\nEnter your desired Fibonacci sequence b1: "))
        b2 = fonk2(b1)
        if b2:
            fonk1(b1, b2)
        b5 = input("\nDo you want to generate another Fibonacci sequence? (yes/no): ")
        if b5.lower() != 'yes':
            print("Exiting the program...")
            break