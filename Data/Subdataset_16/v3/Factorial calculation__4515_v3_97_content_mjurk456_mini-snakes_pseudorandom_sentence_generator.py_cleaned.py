import random
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
def fonk2(b2, b3, b4, b5):
    return (
        f"A {random.choice(b2)} {random.choice(b3)} "
        f"{random.choice(b4)} a {random.choice(b2)} "
        f"{random.choice(b3)} {random.choice(b5)}."
    )
def fonk3():
    while True:
        try:
            b1 = int(input("How many sentences do you want to generate? "))
            if b1 > 0:
                return b1
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def fonk4():
    b2 = fonk1("adjective.txt")
    b3 = fonk1("noun.txt")
    b4 = fonk1("verb.txt")
    b5 = fonk1("adverb.txt")
    b1 = fonk3()
    for _ in range(b1):
        print(fonk2(b2, b3, b4, b5))
if b6 = = "__main__":
    fonk4()