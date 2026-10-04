class BitStream:
    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)
        self.word = 0
        self.pos = 7 if mode[0] == 'w' else -1
        self.mode = mode
    def read(self, size):
        ret = ''
        for _ in range(size):
            if self.pos == -1:
                self.word = self.file.read(1)
                if not self.word:
                    return ret
                self.word = ord(self.word)
                self.pos = 7
            ret += '1' if self.word & (1 << self.pos) else '0'
            self.pos -= 1
        return ret
    def write(self, string):
        for char in string:
            if char not in ('0', '1'):
                continue
            self.word = (self.word << 1) | (1 if char == '1' else 0)
            self.pos -= 1
            if self.pos == -1:
                self.flush()
    def flush(self):
        if self.pos != 7:
            self.word <<= self.pos + 1
            self.file.write(self.word.to_bytes(1, byteorder='little'))
        self.word = 0
        self.pos = 7
    def close(self):
        if self.mode[0] == 'w':
            self.flush()
        self.file.close()
if __name__ == '__main__':
    input_file = BitStream('./test.txt', 'rb')
    output_file = BitStream('./temp.txt', 'wb')
    bit = input_file.read(1)
    while bit:
        print(bit, end='')
        output_file.write(bit)
        bit = input_file.read(1)
    input_file.close()
    output_file.close()