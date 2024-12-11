def fonk1(b8, key):
    b1 = ''
    for char in b8:
        b2 = ord(char)
        if char.isalpha():
            b3 = ord('a') if char.islower() else ord('A')
            b2 = ((b2 - b3 + key) % 26) + b3
        b1 += chr(b2)
    return b1
def fonk2(b6, key):
    b4 = ''
    for char in b6:
        b2 = ord(char)
        if char.isalpha():
            b3 = ord('a') if char.islower() else ord('A')
            b2 = ((b2 - b3 - key) % 26) + b3
        b4 += chr(b2)
    return b4
def fonk3(b8, key):
    b5 = len(key)
    b6 = ''
    for i, char in enumerate(b8):
        if char.isalpha():
            b3 = ord('a') if char.islower() else ord('A')
            b7 = ord(key[i % b5].lower()) - ord('a')
            b2 = ((ord(char) - b3 + b7) % 26) + b3
            b6 += chr(b2)
        else:
            b6 += char
    return b6
def fonk4(b6, key):
    b5 = len(key)
    b8 = ''
    for i, char in enumerate(b6):
        if char.isalpha():
            b3 = ord('a') if char.islower() else ord('A')
            b7 = ord(key[i % b5].lower()) - ord('a')
            b2 = ((ord(char) - b3 - b7) % 26) + b3
            b8 += chr(b2)
        else:
            b8 += char
    return b8