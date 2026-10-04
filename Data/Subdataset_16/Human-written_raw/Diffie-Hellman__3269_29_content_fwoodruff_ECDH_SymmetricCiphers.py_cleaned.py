import TypeConversion as TC
def fonk1(message, symmetricKey58):
    '''
    XOR encrypts a message using a symmetric key
    '''
    b1 = TC.stringToBigInt(message)
    b2 = TC.b58toInt(symmetricKey58)
    b3 = b1 ^ b2
    b4 = TC.intTob58(b3)
    return b4
def fonk2(b4, symmetricKey58):
    '''
    XOR decrypts a message using a symmetric key
    '''
    b5 = TC.b58toInt(b4)
    b6 = TC.b58toInt(symmetricKey58)
    b7 = b5 ^ b6
    b8 = TC.bigIntToString(b7)
    return b8