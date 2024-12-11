import argparse
import numpy, math
from numpy import fft
import wave, struct, math
from scipy.io import wavfile
import numpy as np
b22 = 44100
b1 = b22 / 2.0
b23 = 512
def fonk1(cutoff):
        cutoff /= (b1 / (b23 / 2.0))
        b2 = []
        b3 = []
        b4 = b23
        for f in range(0, b4+1):
                a3 = 1.0
                if f > cutoff:
                        a3 = 0
                b2.append(a3)
                if f > 0 and f < b4:
                        b3.append(a3)
        b3.reverse()
        b2 = b2 + b3
        b5 = fft.ifft(b2).real.tolist()
        b6 = b5[:b23
        b7 = b5[b23
        b5 = b7 + b6
        b8 = b23
        for n in range(0, b8):
                    b5[n] *= (n + 0.0) / b8
        for n in range(b8 + 1, b23):
                    b5[n] *= (b23 - n + 0.0) / b8
        return b5
def fonk2(original, cutoff):
        b9 = fonk1(cutoff)
        return numpy.convolve(original, b9)
def fonk3(inpt1, b35):
    b10 = wave.open(inpt1, mode='rb')
    b11 = bytearray(list(b10.readframes(b10.getnframes())))
    b12 = [b11[i] & 1 for i in range(len(b11))]
    b13 = "".join(chr(int("".join(map(str,b12[i:i+8])),2)) for i in range(0,len(b12),8))
    b14 = b13.split("
    with open(b35, "w") as text_file:
        text_file.write(b14)
    b10.close()
def fonk4(inpt1,b35):
    b15 = wave.open(inpt1, "r")
    b16 = wave.open(b35, "w")
    for f in [b16]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    for n in range(0, b15.getnframes()):
        b17 = struct.unpack('h', b15.readframes(1))[0] / 32768.0
        b18 = math.cos(22050.0 * (n / 44100.0) * math.pi * 2)
        b19 = b17 * b18
        b16.writeframes(struct.pack('h', int(b19* 32767)))
def fonk5(b35):
    rate1, b20 = wavfile.read(b35)
    b20 = 8*fonk2(1/2*b20,4500)
    b21 = b20.astype(np.int16)
    wavfile.write(b35,rate1,b21)
def fonk6(inpt1, b35):
    rate1, b20 = wavfile.read(inpt1)
    b6 = b20[...,0].copy()
    b7 = b20[...,1].copy()
    b22 = b7[0]
    b23 = b7[1]
    b24 = b22*1000+b23
    b25 = np.array([])
    b26 = int((len(b6) / b24 - 1))
    a4 = 4
    a5 = 0
    b27 = []
    while a5 < b24:
        a6 = 0
        a6 += int(np.abs(b7[a4])%10)
        a6 = a6 * 10 + int(np.abs(b6[a4+1])%10)
        a6 = a6 * 10 + int(np.abs(b7[a4+2])%10)
        a6 = a6 * 10 + int(np.abs(b6[a4+3])%10)
        a6 = a6 * 10 + int(np.abs(b7[a4+4])%10)
        b28 = int(np.abs(b6[a4 + 5])%10)
        a6 = a6 * (b28 - 1)
        b27.append(a6)
        a4 += b26
        a5 = a5 + 1
    b25 = np.append(b25, b27)
    wavfile.write(b35,rate1,(b25.T).astype(np.int16))
def fonk7():
    b29 = argparse.ArgumentParser()
    b29.add_argument("INPUT1", b30 = "Name of the wave file")
    b29.add_argument("-t", "--b32", b30 = "Input b32.", action='store_true')
    b29.add_argument("-s", "--b33", b30 = "Input b33 for AM modulation.", action='store_true')
    b29.add_argument("-c", "--b34", b30 = "Input b33 for cypto-stegano.", action='store_true')
    b29.add_argument("-o", "--b35", b30 = "Name of the b35 wav file. Default value: out.wav).")
    b31 = b29.parse_args()
    b32 = True
    b33 = False
    b34 = False
    b35 = "out.wav"
    b36 = "Text"
    a4 = 0
    if b31.b32:
        b32 = b31.b32
        a4 += 1
    if b31.b33:
        b33 = b31.b33
        b36 = "Sound"
        a4 += 1
        b32 = False
    if b31.b34:
        b34 = b31.b34
        b36 = "Crypto"
        a4 += 1
        b32 = False
    if b31.b35:
        b35 = b31.b35
    print('Input file1: %s' % b31.INPUT1)
    print('Operation: %s' % b36)
    print('Output: %s' % b35)
    if a4 > 1:
        print('Error, more the just 1 b36 selected!')
        b32 = b33 = b34 = False
    return (b31.INPUT1,b35, b32, b33, b34)
def fonk8(inpt1, b35):
    fonk3(inpt1, b35)
def fonk9(inpt1, b35):
    fonk4(inpt1, b35)
    fonk5(b35)
def fonk10(inpt1, b35):
    fonk6(inpt1, b35)
if b37 = = '__main__':
    b38 = fonk7()
    if b38[2] == True:
        fonk8(b38[0], b38[1])
    if b38[3] == True:
        fonk9(b38[0], b38[1])
    if b38[4] == True:
        fonk10(b38[0], b38[1])