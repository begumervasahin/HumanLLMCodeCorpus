import numpy as np
import wave
import struct
b1 = {
    1: 'b',
    2: 'h'
}
def fonk1(filename):
    with wave.open(filename, 'r') as file:
        b2 = file.getnchannels()
        b3 = file.getsampwidth()
        b4 = file.getframerate()
        b5 = file.getnframes()
        b6 = f"<{b5}{b1[b3]}"
        b7 = file.readframes(b5)
        b8 = np.array(struct.unpack(b6, b7))
        return b2, b3, b4, b5, b8
def fonk2(filename, headers, b8):
    b2, b3, b4, b5 = headers
    b8 = np.clip(b8[:b5], -2**(b3*8-1), 2**(b3*8-1)-1)
    b6 = f"<{b5}{b1[b3]}"
    with wave.open(filename, 'w') as file:
        file.setnchannels(b2)
        file.setsampwidth(b3)
        file.setframerate(b4)
        file.setnframes(b5)
        b7 = struct.pack(b6, *b8)
        file.writeframes(b7)
