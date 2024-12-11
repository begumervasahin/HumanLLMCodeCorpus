from softAES import _compact_word, AES
import copy
import array
from byte_utils import bytes_from_hex, print_hex_str
class class1(AES):
    def fonk1(self, b17, rounds):
        super().fonk1(b17)
        self.b1 = self.b1[:rounds + 1]
        self.b2 = self.b2[-(rounds + 1):]
        self.b3 = self.b1[-1]
        self.b1[-1] = [0] * 4
        self.b2[0] = [0] * 4
    def fonk2(self, b16, rounds, b4 = True):
        if len(b16) != 16:
            raise ValueError('Invalid block length')
        rounds += 1
        if rounds > len(self.b1):
            raise Exception("Not enough b17 for partial encryption")
        (s1, s2, s3) = [1, 2, 3]
        b5 = [0, 0, 0, 0]
        b6 = [_compact_word(b16[4 * i:4 * i + 4]) ^ self.b1[0][i] for i in range(4)]
        for r in range(1, rounds):
            for i in range(4):
                b5[i] = (
                    self.T1[(b6[i] >> 24) & 0xFF] ^
                    self.T2[(b6[(i + s1) % 4] >> 16) & 0xFF] ^
                    self.T3[(b6[(i + s2) % 4] >> 8) & 0xFF] ^
                    self.T4[b6[(i + s3) % 4] & 0xFF] ^
                    self.b1[r][i]
                )
            b6 = copy.copy(b5)
        b7 = []
        if not b4:
            for i in range(4):
                b6[i] = b6[i] ^ self.b1[rounds-1][i]
        for i in range(4):
            b7.extend([
                (b6[i] >> 24) & 0xFF,
                (b6[i] >> 16) & 0xFF,
                (b6[i] >> 8) & 0xFF,
                b6[i] & 0xFF
            ])
        return b7
    def fonk3(self, b16, rounds):
        b8 = array.array('B', b16)
        b9 = self.fonk2(b8, rounds)
        return "".join(map(chr, b9))
    def fonk4(self, round):
        return self.b1[round]
    def fonk5(self, round):
        b10 = []
        for i in range(4):
            b11 = self.b1[round][i]
            b10.extend([
                (b11 >> 24) & 0xff,
                (b11 >> 16) & 0xff,
                (b11 >> 8) & 0xff,
                (b11 >> 0) & 0xff
            ])
        return b10
    def fonk6(self, round, byte):
        b11 = byte
        b12 = self.fonk4(round)
        b13 = b12[b11]
        b14 = (b13 >> ((3 - byte % 4) * 8)) & 0xff
        return b14
if b15 = = '__main__':
    b16 = '00112233445566778899aabbccddeeff'
    b17 = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
    b18 = '9cf0a62049fd59a399518984f26be178'
    b19 = bytes_from_hex(b17)
    b8 = bytes_from_hex(b16)
    b20 = class1(b19, 5)
    b21 = b20.encrypt(b8)
    b22 = b20.decrypt(b21)
    b23 = b20.fonk2(b8, 1)
    b24 = b20.fonk2(b8, 2)
    b25 = b20.fonk2(b8, 5)
    print_hex_str(b21, 'b21')
    print_hex_str(bytes_from_hex(b18), 'b18')
    print_hex_str(b22)
    print_hex_str(b23)
    print_hex_str(b24)
    print_hex_str(b25)
    print('Testing AES 128')
    b17 = '000102030405060708090a0b0c0d0e0f'
    b19 = bytes_from_hex(b17)
    b20 = class1(b19, 10)
    b26 = AES(b19)
    b27 = b26.encrypt(b8)
    b28 = b20.encrypt(b8)
    b29 = b20.fonk2(b8, 9)
    b30 = b20.fonk2(b8, 9, False)
    b22 = b26.decrypt(b27)
    b23 = b20.fonk2(b8, 1)
    b24 = b20.fonk2(b8, 2)
    b25 = b20.fonk2(b8, 5)
    print('Full encryption:', list(map(hex, b27)))
    print('No last round b17:', list(map(hex, b28)))
    print('After full 9 rounds:', list(map(hex, b29)))
    print('After full 9 rounds without round 9 b17:', list(map(hex, b30)))
    print('Plaintext:', list(map(hex, b22)))
    print('Round 1:', list(map(hex, b23)))
    print('Round 2:', list(map(hex, b24)))
    print('Round 3:', list(map(hex, b25)))