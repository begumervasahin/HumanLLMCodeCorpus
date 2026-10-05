class BitStream:
    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)
        self.word = 0
        self.pos = -1 if mode[0] == 'r' else 7
        self.mode = mode
    def read(self, size):
        ret = ''
        for _ in range(size):
            if self.pos == -1:
                self.word = ord(self.file.read(1)) if (data := self.file.read(1)) else ''
                self.pos = 7
            ret += '1' if self.word & (1 << self.pos) else '0'
            self.pos -= 1
        return ret
    def write(self, string):
        for char in string:
            if char == '0':
                self.word <<= 1
            elif char == '1':
                self.word = (self.word << 1) + 1
            else:
                continue
            self.pos -= 1
            if self.pos == -1:
                self.flush()
    def close(self):
        if self.mode[0] == 'w':
            self.flush()
        self.file.close()
    def flush(self):
        if self.pos != 7:
            self.word <<= (self.pos + 1)
            self.file.write(self.word.to_bytes(1, byteorder='little'))
        self.word = 0
        self.pos = 7
if __name__ == '__main__':
    file_stream = BitStream('./test.txt', 'rb')
    write_stream = BitStream('./temp.txt', 'wb')
    ch = file_stream.read(1)
    i = 0
    while ch:
        print(ch, end='')
        i += 1
        if i % 8 == 0:
            print()
        write_stream.write(ch)
        ch = file_stream.read(1)
    file_stream.close()
    write_stream.close()