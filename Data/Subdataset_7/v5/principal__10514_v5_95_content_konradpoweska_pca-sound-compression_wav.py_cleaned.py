import numpy as np
import wave
import struct
b1 = {
    1: 'b',
    2: 'h'
}
def fonk1(filename):
    with wave.open(filename, 'r') as wav_file:
        b2 = wav_file.getnchannels()
        b3 = wav_file.getsampwidth()
        b4 = wav_file.getframerate()
        b5 = wav_file.getnframes()
        b6 = (b2, b3, b4, b5)
        b7 = f"<{b5}{b1[b3]}"
        b8 = wav_file.readframes(b5)
        b9 = np.array(struct.unpack(b7, b8))
    return b6, b9
def fonk2(filename, b6, b9):
    b2, b3, b4, b5 = b6
    b9 = np.clip(b9[:b5], -2**(b3*8-1), 2**(b3*8-1)-1)
    b7 = f"<{b5}{b1[b3]}"
    b8 = struct.pack(b7, *b9)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(b2)
        wav_file.setsampwidth(b3)
        wav_file.setframerate(b4)
        wav_file.setnframes(b5)
        wav_file.writeframes(b8)