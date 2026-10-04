from Crypto.Cipher import AES
from Crypto import Random
b1 = "4532294977918448"
print 'Number to b2 = ' + b1
b3 = []
def fonk1(b4, b12):
    b4 = '{:032b}'.format(int(b4, 16))
    b5 = ''
    for i in range(len(b4) - 5):
        b5 += str(int(b4[i]) ^ int(b12[i]))
    return b5
def fonk2(card_number, rounds, produce_keys):
    b6 = '{0:054b}'.format(int(card_number))
    b7 = b6[:27]
    b8 = b6[27:]
    if produce_keys:
        for i in range(rounds):
            b9 = Random.new().read(16).encode('hex')
            b3.append(b9)
    for i in range(rounds):
        b9 = b3[i]
        b10 = AES.new(b9.decode('hex'))
        b11 = '{:08x}'.format(int(b8 + '0'*5, 2))
        b12 = b11 + '0'*23 + str(i+1)
        b13 = b10.b2(b12.decode('hex')).encode('hex')[:7] + '0'
        b5 = b8
        b8 = fonk1(b13, b7+'0'*5)
        b7 = b5
    return (b7 , b8)
def fonk3(cipher, rounds):
    b6 = '{0:054b}'.format(int(cipher))
    b7 = b6[:27]
    b8 = b6[27:]
    for i in range(rounds,0,-1):
        b9 = b3[i-1]
        b10 = AES.new(b9.decode('hex'))
        b14 = '{:08x}'.format(int(b7 + '0'*5, 2))
        b12 = b14 + '0'*23 + str(i)
        b13 = b10.b2(b12.decode('hex')).encode('hex')[:7] + '0'
        b5 = b7
        b7 = fonk1(b13, b8+'0'*5)
        b8 = b5
    return (b7 , b8)
b7 , b8 = fonk2(b1, 6, True)
b15 = b7 + b8
b15 = int(b15, 2)
while b15 > 9999999999999999:
    print 'Not valid encoded b16 = ' +  str(b15)
    b7 , b8 = fonk2(b15, 6, False)
    b15 = b7 + b8
    b15 = int(b15, 2)
print 'encoded b16 = ' + str(b15)
print 'Decrypting ...'
print 'Cipher to b17 = ' + str(b15)
b7 , b8 = fonk3(b15, 6)
b15 = b7 + b8
b15 = int(b15, 2)
while b15 > 9999999999999999:
    print 'Not valid encoded b16 = ' +  str(b15)
    b7 , b8 = fonk3(b15, 6)
    b15 = b7 + b8
    b15 = int(b15, 2)
print 'dec b16 = ' + str(b15)