from softAES import _compact_word, AES
import copy
import array
from byte_utils import bytes_from_hex, print_hex_str
class class1(AES):
    def fonk1(self, b17, rounds):
        super(class1, self).fonk1(b17)
        self.b1 = self.b1[0:rounds+1]
        self.b2 = self.b2[-(rounds+1):]
        self.b3 = self.b1[-1]
        self.b1[-1] = [0] * 4
        self.b2[0] = [0] * 4
    def fonk2(self, plaintext, rounds, b4 = True):
        'Encrypt b5 block of plain text using the AES block b29.'
        if len(plaintext) != 16:
            print ('plaintrex len', len(plaintext))
            raise ValueError('wrong block length')
        rounds += 1
        if rounds > len(self.b1) :
            raise Exception("not enough b17 for partial encryption")
        (s1, s2, s3) = [1, 2, 3]
        b5 = [0, 0, 0, 0]
        b6 = [(_compact_word(plaintext[4 * i:4 * i + 4]) ^ self.b1[0][i]) for i in xrange(0, 4)]
        for r in xrange(1, rounds):
            for i in xrange(0, 4):
                b5[i] = (self.T1[(b6[ i          ] >> 24) & 0xFF] ^
                        self.T2[(b6[(i + s1) % 4] >> 16) & 0xFF] ^
                        self.T3[(b6[(i + s2) % 4] >>  8) & 0xFF] ^
                        self.T4[ b6[(i + s3) % 4]        & 0xFF] ^
                        self.b1[r][i])
            b6 = copy.copy(b5)
        b7 = [ ]
        if not b4:
            for i in xrange(0, 4):
                b6[i] = b6[i] ^ self.b1[rounds-1][i]
        for i in xrange(0, 4):
            b7.append((b6[i] >> 24) & 0xFF)
            b7.append((b6[i] >> 16) & 0xFF)
            b7.append((b6[i] >> 8) & 0xFF)
            b7.append(b6[i]        & 0xFF)
        return b7
    def fonk3(self, plaintext, rounds):
        b8 = array.array('B', plaintext)
        b9 = self.fonk2(b8, rounds)
        return "".join(map(chr, b9))
    def fonk4(self, round):
        return self.b1[round]
    def fonk5(self, round):
        b10 = []
        for i in range(4):
            b11 = self.b1[round][i]
            b10.append((b11 >> 24) & 0xff)
            b10.append((b11 >> 16) & 0xff)
            b10.append((b11 >> 8) & 0xff)
            b10.append((b11 >> 0) & 0xff)
        return b10
    def fonk6(self, round, byte):
        b11 = int(byte / 4)
        b12 = self.fonk4(round)
        b13 = b12[b11]
        b14 = (b13 >> ((3-byte % 4) * 8)) & 0xff
        return b14
if b15 = = '__main__':
    b16 = '00112233445566778899aabbccddeeff'
    b17 = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
    b18 = '8ea2b7ca516745bfeafc49904b496089'
    b19 = 'c357aae11b45b7b0a2c7bd28a8dc99fa'
    b19 = 'aeb65ba974e0f822d73f567bdb64c877'
    b19 = '9cf0a62049fd59a399518984f26be178'
    b20 = bytes_from_hex(b17)
    b21 = bytes_from_hex(b16)
    print (b21)
    print (len(b20), b20)
    print (len(b21), b21)
    b22 = class1(b20, 5)
    b23 = b22.encrypt(b21)
    b24 = b22.decrypt(b23)
    b25 = b22.fonk2(b21, 1)
    b26 = b22.fonk2(b21, 2)
    b27 = b22.fonk2(b21, 5)
    print_hex_str(b23, 'b23')
    print_hex_str(bytes_from_hex(b19), 'b19    ')
    print_hex_str(b24)
    print_hex_str(b25)
    print_hex_str(b26)
    print_hex_str(b27)
    print ('test b22 128')
    b17 = '000102030405060708090a0b0c0d0e0f'
    b20 = bytes_from_hex(b17)
    b22 = class1(b20, 10)
    b28 = AES(b20)
    b29 = b28.encrypt(b21)
    b30 = b22.encrypt(b21)
    b31 = b22.fonk2(b21, 9)
    b32 = b22.fonk2(b21, 9, False)
    b24 = b28.decrypt(b29)
    b25 = b22.fonk2(b21, 1)
    b26 = b22.fonk2(b21, 2)
    b27 = b22.fonk2(b21, 5)
    print('full encryption ' ,map(hex, b29))
    print ('no last round b17 ' ,map(hex, b30))
    print ('after full 9 rounds ', map(hex, b31))
    print ('after full 9 rounds no round 9 b17 ', map(hex, b32))
    print (list(map(hex, b24)))
    print (list(map(hex, b25)))
    print (list(map(hex, b26)))
    print (list(map(hex, b27)))
    print (list(map(hex, b22.fonk4(9))))
    print (list(map(hex, b22.b3)))
    print ('test get b17')
    print (list(map(hex, b20)))
    b33 = b22.fonk4(0)
    for i in range(len(b20)):
        print (hex(b22.fonk6(0,i)),)
    print ('')
    for i in range(len(b33)):
        print (hex(b33[i]),)
    print( '')