from softAES import _compact_word, AES
import copy
import array
from byte_utils import bytes_from_hex, print_hex_str
class class1(AES):
    def fonk1(self, b19, rounds):
        super().fonk1(b19)
        self.b1 = self.b1[:rounds + 1]
        self.b2 = self.b2[-(rounds + 1):]
        self.b3 = self.b1[-1]
        self.b1[-1] = [0] * 4
        self.b2[0] = [0] * 4
    def fonk2(self, b18, rounds, b4 = True):
        if len(b18) != 16:
            raise ValueError('Invalid block length')
        rounds += 1
        if rounds > len(self.b1):
            raise Exception("Not enough b19 for partial encryption")
        b5 = [1, 2, 3]
        b6 = [0, 0, 0, 0]
        b7 = [_compact_word(b18[4 * i:4 * i + 4]) ^ self.b1[0][i] for i in range(4)]
        for r in range(1, rounds):
            for i in range(4):
                b6[i] = (
                    self.T1[(b7[i] >> 24) & 0xFF] ^
                    self.T2[(b7[(i + b5[0]) % 4] >> 16) & 0xFF] ^
                    self.T3[(b7[(i + b5[1]) % 4] >> 8) & 0xFF] ^
                    self.T4[b7[(i + b5[2]) % 4] & 0xFF] ^
                    self.b1[r][i]
                )
            b7 = copy.copy(b6)
        b8 = []
        if not b4:
            for i in range(4):
                b7[i] ^= self.b1[rounds - 1][i]
        for i in range(4):
            b8.extend([
                (b7[i] >> 24) & 0xFF,
                (b7[i] >> 16) & 0xFF,
                (b7[i] >> 8) & 0xFF,
                b7[i] & 0xFF
            ])
        return b8
    def fonk3(self, b18, rounds):
        b9 = array.array('B', b18)
        b10 = self.fonk2(b9, rounds)
        return "".join(map(chr, b10))
    def fonk4(self, round):
        return self.b1[round]
    def fonk5(self, round):
        b11 = []
        for i in range(4):
            b12 = self.b1[round][i]
            b11.extend([
                (b12 >> 24) & 0xff,
                (b12 >> 16) & 0xff,
                (b12 >> 8) & 0xff,
                (b12 >> 0) & 0xff
            ])
        return b11
    def fonk6(self, round, byte):
        b13 = byte
        b14 = self.fonk4(round)
        b15 = b14[b13]
        b16 = (b15 >> ((3 - byte % 4) * 8)) & 0xff
        return b16
if b17 = = '__main__':
    b18 = '00112233445566778899aabbccddeeff'
    b19 = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
    b20 = '9cf0a62049fd59a399518984f26be178'
    b21 = bytes_from_hex(b19)
    b9 = bytes_from_hex(b18)
    b22 = class1(b21, 5)
    b23 = b22.encrypt(b9)
    b24 = b22.decrypt(b23)
    b25 = b22.fonk2(b9, 1)
    b26 = b22.fonk2(b9, 2)
    b27 = b22.fonk2(b9, 5)
    print_hex_str(b23, 'b23')
    print_hex_str(bytes_from_hex(b20), 'b20')
    print_hex_str(b24)
    print_hex_str(b25)
    print_hex_str(b26)
    print_hex_str(b27)
    print('Testing AES 128')
    b19 = '000102030405060708090a0b0c0d0e0f'
    b21 = bytes_from_hex(b19)
    b22 = class1(b21, 10)
    b28 = AES(b21)
    b29 = b28.encrypt(b9)
    b30 = b22.encrypt(b9)
    b31 = b22.fonk2(b9, 9)
    b32 = b22.fonk2(b9, 9, False)
    b24 = b28.decrypt(b29)
    b25 = b22.fonk2(b9, 1)
    b26 = b22.fonk2(b9, 2)
    b27 = b22.fonk2(b9, 5)
    print('Full encryption:', list(map(hex, b29)))
    print('No last round b19:', list(map(hex, b30)))
    print('After full 9 rounds:', list(map(hex, b31)))
    print('After full 9 rounds without round 9 b19:', list(map(hex, b32)))
    print('Plaintext:', list(map(hex, b24)))
    print('Round 1:', list(map(hex, b25)))
    print('Round 2:', list(map(hex, b26)))
    print('Round 3:', list(map(hex, b27)))