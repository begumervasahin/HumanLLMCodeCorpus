class BitStream:
    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)
        self.word = 0
        self.mode = mode
        self.pos = 7 if 'w' in mode else -1
    def read(self, size):
        bits = []
        for _ in range(size):
            if self.pos == -1:
                byte = self.file.read(1)
                if not byte:
                    break
                self.word = ord(byte)
                self.pos = 7
            bits.append('1' if self.word & (1 << self.pos) else '0')
            self.pos -= 1
        return ''.join(bits)
    def write(self, bit_string):
        for bit in bit_string:
            if bit not in ('0', '1'):
                continue
            self.word = (self.word << 1) | int(bit)
            self.pos -= 1
            if self.pos == -1:
                self._flush()
    def _flush(self):
        if self.pos != 7:
            padded_word = self.word << (self.pos + 1)
            self.file.write(padded_word.to_bytes(1, byteorder='little'))
        self.word = 0
        self.pos = 7
    def close(self):
        if 'w' in self.mode:
            self._flush()
        self.file.close()
if __name__ == '__main__':
    input_file = BitStream('./test.txt', 'rb')
    output_file = BitStream('./temp.txt', 'wb')
    while True:
        bit = input_file.read(1)
        if not bit:
            break
        print(bit, end='')
        output_file.write(bit)
    input_file.close()
    output_file.close()