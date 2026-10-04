def fonk1( key, text ):
    b1 = ""
    a1 = 0
    for char in text:
        b1 += chr(ord(char) ^ ord(key[a1]))
        a1 += 1
        if a1 = =len(key):
            a1 = 0
    return b1