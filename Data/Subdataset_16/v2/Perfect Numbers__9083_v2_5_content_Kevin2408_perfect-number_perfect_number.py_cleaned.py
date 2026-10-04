def fonk1(b2: int) -> None:
    for number in range(2, b2):
        b1 = sum(divisor for divisor in range(1, number) if number % divisor == 0)
        if b1 = = number:
            print(number)
def fonk2() -> None:
    try:
        b2 = int(input("Input the range number: "))
        if b2 < 2:
            print("Please enter a number greater than or equal to 2.")
            return
        fonk1(b2)
    except ValueError:
        print("Please enter a valid integer.")
if b3 = = "__main__":
    fonk2()