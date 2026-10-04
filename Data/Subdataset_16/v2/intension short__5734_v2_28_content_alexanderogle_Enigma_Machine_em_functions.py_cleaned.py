def fonk1(b8):
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b2 = b1.index(b8)
    return b1[b2:] + b1[:b2]
def fonk2(text, b8):
    print(f"\nOriginal Text: {text}")
    b3 = fonk1(b8)
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b4 = ''.join(
        b3[b1.index(char)] if char.isalpha() else char for char in text
    )
    print(f"\nKey Letter: {b8}")
    print("Substitution Alphabet: <", ' '.join(b3), ">")
    return b4
def fonk3(encoded_text, b8):
    print(f"\nEncoded Text: {encoded_text}")
    b3 = fonk1(b8)
    b1 = list("abcdefghijklmnopqrstuvwxyz")
    b5 = ''.join(
        b1[b3.index(char)] if char.isalpha() else char for char in encoded_text
    )
    print(f"\nKey Letter: {b8}")
    print("Substitution Alphabet: <", ' '.join(b3), ">")
    return b5
def fonk4(text):
    print(" ".join(text))
def fonk5(size):
    return [0] * size
def fonk6(letter):
    if len(letter) != 1 or not letter.isalpha():
        print("That's not a letter!")
        return None
    return ord(letter.lower()) - ord('a')
if b6 = = "__main__":
    b7 = "hello world"
    b8 = 'd'
    b4 = fonk2(b7, b8)
    print(f"\nEncoded Message: {b4}")
    b5 = fonk3(b4, b8)
    print(f"\nDecoded Message: {b5}")
    print("\nOutput Encoded Message:")
    fonk4(b4)
    print("\nEmpty Array Example:", fonk5(5))
    print(f"Index of '{b8}' in Alphabet:", fonk6(b8))