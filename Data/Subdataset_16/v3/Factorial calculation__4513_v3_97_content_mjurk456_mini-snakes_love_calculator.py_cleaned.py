def fonk1(source, characters):
    return sum(1 for char in source if char in characters)
def fonk2(name1, b4):
    b1 = "aeiou"
    b2 = "qrtpsdfghjklzxcvbnmy"
    a1 = 0
    if name1[0] == b4[0]:
        a1 += 20
    if name1[0] in b1 and b4[0] in b1:
        a1 += 10
    if name1[0] in b2 and b4[0] in b2:
        a1 += 5
    if fonk1(name1, b1) == fonk1(b4, b1):
        a1 += 12
    if fonk1(name1, b2) == fonk1(b4, b2):
        a1 += 12
    if any(letter in name1 and letter in b4 for letter in 'love'):
        a1 += 7
    return a1
def fonk3():
    while True:
        try:
            b3 = input("Enter two names separated by a comma (e.g., 'Jan, Joanna'): ").strip()
            name1, b4 = [name.strip().lower() for name in b3.split(",")]
            a1 = fonk2(name1, b4)
            print(f"Your love points are {a1}.")
            print("REMEMBER: your relationship depends on you and your partner, not on this silly love calculator!")
            break
        except ValueError:
            print("Invalid input. Please enter two names separated by a comma.")
if b5 = = "__main__":
    fonk3()