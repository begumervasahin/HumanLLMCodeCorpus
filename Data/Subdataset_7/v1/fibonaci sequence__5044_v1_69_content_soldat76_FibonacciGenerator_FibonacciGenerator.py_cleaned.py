def fonk1(b1, b2):
    print(f"\nHere is your Fibonacci sequence of {b2} number(s):\n\t{b1}")
def fonk2(b2):
    b1 = [1, 1]
    if b2 <= 0:
        print("The sequence must contain some positive number.")
        return None
    elif b2 = = 1:
        return [1]
    elif b2 = = 2:
        return b1
    else:
        for i in range(2, b2):
            b3 = b1[-1] + b1[-2]
            b1.append(b3)
        return b1
if b4 = = "__main__":
    print("\nThis program will print out a Fibonacci sequence of your desired b2!")
    while True:
        b2 = int(input("\nEnter your desired Fibonacci sequence b2: "))
        b1 = fonk2(b2)
        if b1:
            fonk1(b1, b2)
        b5 = input("\nDo you want to generate another Fibonacci sequence? (yes/no): ")
        if b5.lower() != 'yes':
            print("Exiting the program...")
            break