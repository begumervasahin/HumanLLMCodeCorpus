def fonk1(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        print("Invalid input: Please enter an integer.")
        return False
def fonk2(number):
    if number <= 1:
        print(f"{number} is not a prime number.")
        return False
    for b1 in range(2, int(number**0.5) + 1):
        if number % b1 = = 0:
            print(f"{number} is not a prime number.")
            return False
    print(f"{number} is a prime number.")
    return True
def fonk3():
    while True:
        b2 = input("Enter a Number (or 'stop' to quit): ")
        if b2.lower() == "stop":
            print("Exiting the program.")
            break
        if fonk1(b2):
            fonk2(int(b2))
if b3 = = "__main__":
    fonk3()