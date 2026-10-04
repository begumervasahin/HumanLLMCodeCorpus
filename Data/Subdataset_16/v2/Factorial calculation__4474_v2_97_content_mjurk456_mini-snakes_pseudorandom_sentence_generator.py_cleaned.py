import random
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    return [word.strip() for word in b1]
def fonk2(b2, b3, b4, b5):
    return (
        f"A {random.choice(b2)} {random.choice(b3)} "
        f"{random.choice(b4)} a {random.choice(b2)} "
        f"{random.choice(b3)} {random.choice(b5)}."
    )
def fonk3():
    b2 = fonk1("adjective.txt")
    b3 = fonk1("noun.txt")
    b4 = fonk1("verb.txt")
    b5 = fonk1("adverb.txt")
    while True:
        try:
            b6 = int(input("How many sentences do you want to generate? "))
            if b6 <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    for _ in range(b6):
        print(fonk2(b2, b3, b4, b5))
if b7 = = "__main__":
    fonk3()