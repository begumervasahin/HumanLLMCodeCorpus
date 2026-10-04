def fonk1(b2, b1):
    if b1 = = 0:
        return b2
    if b2 = = 0:
        return b1
    if b2 > b1:
        return fonk1(b2 - b1, b1)
    else:
        return fonk1(b2, b1 - b2)
def fonk2(b2, b1):
    if b1 = = 0:
        return b2
    else:
        return fonk2(b1, b2 % b1)
def fonk3():
    while True:
        b3 = input("Choose algorithm - Classic (c) or Modern (m) Euclidean: ").lower()
        if b3 not in ['c', 'm']:
            print("Invalid choice. Please choose 'c' for Classic or 'm' for Modern.")
            continue
        while True:
            b4 = input("Enter b2 number (or type 'exit' to choose algorithm again): ")
            if b4.lower() == 'exit':
                break
            if b4.isnumeric():
                b2 = int(b4)
                b1 = int(input("Enter the second number: "))
                if b3 = = 'c':
                    b5 = fonk1(b2, b1)
                else:
                    b5 = fonk2(b2, b1)
                print(f"The GCD of {b2} and {b1} is: {b5}")
            else:
                print("Invalid input. Please enter b2 numeric value.")
if b6 = = "__main__":
    fonk3()