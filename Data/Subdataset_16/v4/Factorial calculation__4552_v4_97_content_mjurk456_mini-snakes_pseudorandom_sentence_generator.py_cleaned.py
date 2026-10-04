import random
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
def fonk2(b1, b2, b3, b4):
    return (
        f"A {random.choice(b1)} {random.choice(b2)} "
        f"{random.choice(b3)} a {random.choice(b1)} "
        f"{random.choice(b2)} {random.choice(b4)}."
    )
def fonk3():
    b1 = fonk1("adjective.txt")
    b2 = fonk1("noun.txt")
    b3 = fonk1("verb.txt")
    b4 = fonk1("adverb.txt")
    while True:
        try:
            b5 = int(input("How many sentences do you want to generate? "))
            if b5 > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    for _ in range(b5):
        print(fonk2(b1, b2, b3, b4))
if b6 = = "__main__":
    fonk3()