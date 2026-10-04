def fonk1(n):
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b2 = b1.index(n)
    return b1[b2:] + b1[:b2]
def fonk2(text, n):
    print("\nOriginal Text:", text)
    b3 = fonk1(n)
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b4 = ''.join(b3[b1.index(char)] if char.isalpha() else char for char in text)
    print("\nKey Letter:", n)
    print("Substitution Alphabet: <", ' '.join(b3), ">")
    return b4
def fonk3(text, n):
    print("\nEncoded Text:", text)
    b3 = fonk1(n)
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b5 = ''.join(b1[b3.index(char)] if char.isalpha() else char for char in text)
    print("\nKey Letter:", n)
    print("Substitution Alphabet: <", ' '.join(b3), ">")
    return b5
def fonk4(text):
    for char in text:
        print(char, b6 = " ")
def fonk5(size):
    return [0] * size
def fonk6(letter):
    if len(letter) != 1 or not letter.isalpha():
        print("That's not a letter!")
        return None
    return ord(letter.lower()) - ord('a')
if b7 = = "__main__":
    b8 = "hello world"
    b9 = 'd'
    b10 = fonk2(b8, b9)
    print("\nEncoded Message:", b10)
    b11 = fonk3(b10, b9)
    print("\nDecoded Message:", b11)
    fonk4(b10)
    print("\n")
    print("Empty Array:", fonk5(5))
    print("Index of 'd' in Alphabet:", fonk6('d'))