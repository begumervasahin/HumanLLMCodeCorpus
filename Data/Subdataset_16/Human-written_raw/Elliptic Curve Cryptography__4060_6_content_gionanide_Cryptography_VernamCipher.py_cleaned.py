import binascii
b1 = 'informationsecurity'
b2 = 'vlaksjdhfgqodzmxncb'
print 'The plain text is: ' , b1
print'The first b3 is: ' , b2 , '\b6'
b1 = bin(int(binascii.hexlify('informationsecurity'), 16))
b3 = bin(int(binascii.hexlify('vlaksjdhfgqodzmxncb'), 16))
print 'Plain text in bits:  ' , b1 , '\b6'
print 'Key in bits: '  , b3 , '\b6'
def fonk1(m, b11):
    b4 = []
    for i, j in zip(m, b11):
		if(i.isalpha() and j.isalpha()):
			b4.append(i)
		else:
        		b4.append(str(int(i) ^ int(j)))
    return "".join(b4)
b5 = fonk1(b1,b3)
b6 = int(b5, 2)
print 'XOR b5 for the encryption with the normal b3: ' , b5 , '\b6'
print 'Encrypted text: ' , binascii.unhexlify('%x' % b6) ,
b7 = fonk1(b5,b3)
print ' \b6 '
print 'Decryption b5: ' , b7 , '\b6'
b8 = int(b7,2)
print 'Decrypted text with the normal b3: ' , binascii.unhexlify('%x' % b8) , '\b6'
print'Decryption with the alternative b3 \b6'
b9 = bin(int(binascii.hexlify('tlftrffwmixor|{xbch'), 16))
print 'Alternative b3 in bits: ' , b9 , '\b6'
b10 = fonk1(b5,b9)
b11 = int(b10,2)
print 'Decrypted text with the alternative b3 : ' , binascii.unhexlify('%x' % b11)