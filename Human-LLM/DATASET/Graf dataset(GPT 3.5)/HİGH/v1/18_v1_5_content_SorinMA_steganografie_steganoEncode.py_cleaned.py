import argparse
import math
import struct
import wave
from scipy.io import wavfile
import numpy as np
from numpy import fft
a1 = 44100
b1 = a1 / 2.0
a2 = 512
def fonk1(cutoff):
    cutoff /= (b1 / (a2 / 2.0))
    b2 = []
    b3 = []
    b4 = a2
    for f in range(0, b4 + 1):
        a3 = 1.0
        if f > cutoff:
            a3 = 0
        b2.append(a3)
        if 0 < f < b4:
            b3.append(a3)
    b3.reverse()
    b2 = b2 + b3
    b5 = fft.ifft(b2).real.tolist()
    b6 = b5[:a2
    b7 = b5[a2
    b5 = b7 + b6
    b8 = a2
    for n in range(0, b8):
        b5[n] *= (n + 0.0) / b8
    for n in range(b8 + 1, a2):
        b5[n] *= (a2 - n + 0.0) / b8
    return b5
def fonk2(original, cutoff):
    b9 = fonk1(cutoff)
    return np.convolve(original, b9)
def fonk3(b38, filtr):
    rate, b10 = wavfile.read(b38)
    try:
        b11 = len(b10[0])
        b12 = np.array([0] * len(b10[..., 0])).astype(np.float)
        for i in range(b11):
            b12 += 1 / b11 * b10[..., i].astype(np.float)
        if filtr:
            b12 = 2 * fonk2(1 / 2 * b12, 4500)
        wavfile.write('b27' + b38, rate, b12.astype(np.int16))
        print('Step - ok')
    except Exception as e:
        print(f'Exception: {e}')
        if filtr:
            b10 = 2 * fonk2(1 / 2 * b10, 4500)
        wavfile.write('b27' + b38, rate, b10.astype(np.int16))
        print('Step - ok but exception')
def fonk4(inpt1, inpt2, b35):
    b13 = wave.open(inpt1, mode='rb')
    b14 = bytearray(list(b13.readframes(b13.getnframes())))
    with open(inpt2, 'r') as file:
        b15 = file.read().replace('\n', '')
    b15 = b15 + int((len(b14) - (len(b15) * 8 * 8)) / 8) * ' '
    b16 = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in b15])))
    if len(b16) < b13.getnframes():
        for i, bit in enumerate(b16):
            b14[i] = (b14[i] & 254) | bit
        b17 = bytes(b14)
        with wave.open(b35, 'wb') as fd:
            fd.setparams(b13.getparams())
            fd.writeframes(b17)
        b13.close()
    else:
        print("Bits overflow for stegano, but we still but a piece of msg in your b10 carrier!")
        a4 = 0
        for i, bit in enumerate(b16):
            if a4 < b13.getnframes():
                b14[i] = (b14[i] & 254) | bit
                a4 += 1
            else:
                break
        b17 = bytes(b14)
        with wave.open(b35, 'wb') as fd:
            fd.setparams(b13.getparams())
            fd.writeframes(b17)
        b13.close()
def fonk5(inpt1, inpt2, b35):
    b18 = wave.open('b27' + inpt1, "r")
    b19 = wave.open('b27' + inpt2, "r")
    b20 = wave.open(b35, "w")
    for f in [b20]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    a4 = 0
    for n in range(0, b18.getnframes()):
        b21 = (struct.unpack('h', b18.readframes(1))[0] / 32768.0) / 2
        if a4 < b19.getnframes():
            b22 = struct.unpack('h', b19.readframes(1))[0] / 32768.0
            b23 = math.cos(22050.0 * (a4 / 44100.0) * math.pi * 2)
            b21 += b22 * b23 / 4
            a4 += 1
        b20.writeframes(struct.pack('h', int(b21 * 32767)))
def fonk6(inpt1, inpt2, b35):
    rate1, b24 = wavfile.read(inpt1)
    rate2, b25 = wavfile.read('b27' + inpt2)
    b6 = b24[..., 0].copy()
    b7 = b24[..., 1].copy()
    b6[0] = b7[0] = len(b25) / 1000.0
    b6[1] = b7[1] = len(b25) % 1000.0
    a4 = 4
    b26 = int((len(b6) / len(b25) - 1))
    if b26 >= 6:
        print("OK")
        a5 = 0
        while a5 < len(b25):
            b27 = int(np.abs(b25[a5]))
            b6[a4 + 5] = np.sign(b6[a4 + 5]) * (
                    (int(np.abs(b6[a4 + 5]) / 10) * 10) + 1 + np.sign(b25[a5]))
            b7[a4 + 4] = np.sign(b7[a4 + 4]) * (
                    (int(np.abs(b7[a4 + 4]) / 10) * 10) + int(np.abs(b27) % 10))
            b27 = int(b27 / 10)
            b6[a4 + 3] = np.sign(b6[a4 + 3]) * (
                    (int(np.abs(b6[a4 + 3]) / 10) * 10) + int(np.abs(b27) % 10))
            b27 = int(b27 / 10)
            b7[a4 + 2] = np.sign(b7[a4 + 2]) * (
                    (int(np.abs(b7[a4 + 2]) / 10) * 10) + int(np.abs(b27) % 10))
            b27 = int(b27 / 10)
            b6[a4 + 1] = np.sign(b6[a4 + 1]) * (
                    (int(np.abs(b6[a4 + 1]) / 10) * 10) + int(np.abs(b27) % 10))
            b27 = int(b27 / 10)
            b7[a4] = np.sign(b7[a4]) * (
                    (int(np.abs(b7[a4]) / 10) * 10) + int(np.abs(b27) % 10))
            a4 += b26
            a5 += 1
        b28 = np.column_stack((b6, b7)).astype(np.int16)
        wavfile.write(b35, rate1, b28)
    else:
        print('Your carrier should be min 6x longer than your message for this kind of stegano')
def fonk7():
    b29 = argparse.ArgumentParser()
    b29.add_argument("INPUT1", b30 = "Name of the wave file")
    b29.add_argument("INPUT2", b30 = "Name of the wave or txt file")
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
    print('Input file2: %s' % b31.INPUT2)
    print('Operation: %s' % b36)
    print('Output: %s' % b35)
    if a4 != 1:
        print('Error: Exactly one b36 should be selected!')
        b32 = b33 = b34 = False
    return (b31.INPUT1, b31.INPUT2, b35, b32, b33, b34)
def fonk8(inpt1, inpt2, b35):
    fonk4(inpt1, inpt2, b35)
def fonk9(inpt1, inpt2, b35):
    fonk3(inpt2, True)
    fonk3(inpt1, False)
    fonk5(inpt1, inpt2, b35)
def fonk10(inpt1, inpt2, b35):
    fonk3(inpt2, False)
    fonk6(inpt1, inpt2, b35)
if b37 = = '__main__':
    b38 = fonk7()
    if b38[3]:
        fonk8(b38[0], b38[1], b38[2])
    elif b38[4]:
        fonk9(b38[0], b38[1], b38[2])
    elif b38[5]:
        fonk10(b38[0], b38[1], b38[2])