import codecs
def fonk1():
    b1 = []
    for i in range(256):
        b2 = i
        for j in range(8):
            if b2 & 1:
                b2 >>= 1
                b2 ^= 0xEDB88320
            else:
                b2 >>= 1
        b1.append(b2)
    return b1
def fonk2(buf):
    b3 = 0xffffffff
    for k in buf:
        b3 = (b3 >> 8) ^ b4[(b3 & 0xff) ^ k]
    return b3 ^ 0xffffffff
b4 = fonk1()
b5 = 'FAFAFA'
b6 = bin(int(b5, 16))
print ("Ulazna poruka je: %s (%s)" %(b6, '0x' + b5))
b7 = fonk2(codecs.decode(b5, 'hex'))
print ("Rezultat je: %s (%s)" %(bin(b7), hex(b7)))
b8 = b6 + bin(b7)[2:]
print("Poruka koja se salje je: ")
print (b8)