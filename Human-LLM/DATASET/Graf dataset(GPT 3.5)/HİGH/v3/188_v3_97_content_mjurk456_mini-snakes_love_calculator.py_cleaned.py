def fonk1(source, example):
    return sum(1 for char in source if char in example)
a1 = 0
b1 = "aeiuo"
b2 = "qrtpsdfghjklzxcvbnmy"
while True:
    try:
        b4, b3 = input("Input two names divided by comma (e.g. 'Jan, Joanna'): ").split(",")
        b4 = b4.lower().strip()
        b3 = b3.lower().strip()
        break
    except ValueError:
        print("Invalid input. Please provide two names separated by comma.")
if b4[0] == b3[0]:
    a1 += 20
if b4[0] in b1 and b3[0] in b1:
    a1 += 10
if b4[0] in b2 and b3[0] in b2:
    a1 += 5
if fonk1(b4, b1) == fonk1(b3, b1):
    a1 += 12
if fonk1(b4, b2) == fonk1(b3, b2):
    a1 += 12
if any(char in b4 and char in b3 for char in 'love'):
    a1 += 7
print(f"Your love points are {a1}")
print("REMEMBER: Your relationship depends only on you and your partner, not on the stupid love calculator!")