import random
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    return [word.strip() for word in b1]
def fonk2(b3, b4, b5, b6):
    b2 = (
        f"A {random.choice(b3)} {random.choice(b4)} "
        f"{random.choice(b5)} a {random.choice(b3)} "
        f"{random.choice(b4)} {random.choice(b6)}."
    )
    return b2
def fonk3():
    b3 = fonk1("adjective.txt")
    b4 = fonk1("noun.txt")
    b5 = fonk1("verb.txt")
    b6 = fonk1("adverb.txt")
    while True:
        try:
            b7 = int(input("How many sentences do you want to generate? "))
            if b7 <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    for _ in range(b7):
        print(fonk2(b3, b4, b5, b6))
if b8 = = "__main__":
    fonk3()