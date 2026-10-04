import TypeConversion as TC
def fonk1(message, symmetric_key_b58):
    b1 = TC.string_to_big_int(message)
    b2 = TC.b58_to_int(symmetric_key_b58)
    b3 = b1 ^ b2
    b4 = TC.int_to_b58(b3)
    return b4
def fonk2(b4, symmetric_key_b58):
    b3 = TC.b58_to_int(b4)
    b2 = TC.b58_to_int(symmetric_key_b58)
    b5 = b3 ^ b2
    b6 = TC.big_int_to_string(b5)
    return b6