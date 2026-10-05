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
def fonk3(input_file, apply_filter):
    rate, b10 = wavfile.read(input_file)
    try:
        b11 = len(b10[0])
        b12 = np.array([0] * len(b10[..., 0])).astype(np.float)
        for i in range(b11):
            b12 += 1 / b11 * b10[..., i].astype(np.float)
        if apply_filter:
            b12 = 2 * fonk2(1 / 2 * b12, 4500)
        b13 = 'b28' + input_file
        wavfile.write(b13, rate, b12.astype(np.int16))
        print('Step - Successful')
    except Exception as e:
        print(f'Exception occurred: {e}')
        if apply_filter:
            b10 = 2 * fonk2(1 / 2 * b10, 4500)
        b13 = 'b28' + input_file
        wavfile.write(b13, rate, b10.astype(np.int16))
        print('Step - Successful, but encountered exception')
def fonk4(input_audio, input_text, b13):
    b14 = wave.open(input_audio, mode='rb')
    b15 = bytearray(list(b14.readframes(b14.getnframes())))
    with open(input_text, 'r') as file:
        b16 = file.read().replace('\n', '')
    b16 = b16 + int((len(b15) - (len(b16) * 8 * 8)) / 8) * ' '
    b17 = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in b16])))
    if len(b17) < b14.getnframes():
        for i, bit in enumerate(b17):
            b15[i] = (b15[i] & 254) | bit
        b18 = bytes(b15)
        with wave.open(b13, 'wb') as fd:
            fd.setparams(b14.getparams())
            fd.writeframes(b18)
        b14.close()
    else:
        print("Bits overflow for steganography, but still embedding part of the message in your b10 carrier!")
        a4 = 0
        for i, bit in enumerate(b17):
            if a4 < b14.getnframes():
                b15[i] = (b15[i] & 254) | bit
                a4 += 1
            else:
                break
        b18 = bytes(b15)
        with wave.open(b13, 'wb') as fd:
            fd.setparams(b14.getparams())
            fd.writeframes(b18)
        b14.close()
def fonk5(input_audio1, input_audio2, b13):
    b19 = wave.open('b28' + input_audio1, "r")
    b20 = wave.open('b28' + input_audio2, "r")
    b21 = wave.open(b13, "w")
    for f in [b21]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    a4 = 0
    for n in range(0, b19.getnframes()):
        b22 = (struct.unpack('h', b19.readframes(1))[0] / 32768.0) / 2
        if a4 < b20.getnframes():
            b23 = struct.unpack('h', b20.readframes(1))[0] / 32768.0
            b24 = math.cos(22050.0 * (a4 / 44100.0) * math.pi * 2)
            b22 += b23 * b24 / 4
            a4 += 1
        b21.writeframes(struct.pack('h', int(b22 * 32767)))
def fonk6(input_audio1, input_audio2, b13):
    rate1, b25 = wavfile.read(input_audio1)
    rate2, b26 = wavfile.read('b28' + input_audio2)
    b6 = b25[..., 0].copy()
    b7 = b25[..., 1].copy()
    b6[0] = b7[0] = len(b26) / 1000.0
    b6[1] = b7[1] = len(b26) % 1000.0
    a4 = 4
    b27 = int((len(b6) / len(b26) - 1))
    if b27 >= 6:
        print("OK")
        a5 = 0
        while a5 < len(b26):
            b28 = int(np.abs(b26[a5]))
            b6[a4 + 5] = np.sign(b6[a4 + 5]) * ((int(np.abs(b6[a4 + 5]) / 10) * 10) + 1 + np.sign(b26[a5]))
            b7[a4 + 4] = np.sign(b7[a4 + 4]) * ((int(np.abs(b7[a4 + 4]) / 10) * 10) + int(np.abs(b28) % 10))
            b28 = int(b28 / 10)
            b6[a4 + 3] = np.sign(b6[a4 + 3]) * ((int(np.abs(b6[a4 + 3]) / 10) * 10) + int(np.abs(b28) % 10))
            b28 = int(b28 / 10)
            b7[a4 + 2] = np.sign(b7[a4 + 2]) * ((int(np.abs(b7[a4 + 2]) / 10) * 10) + int(np.abs(b28) % 10))
            b28 = int(b28 / 10)
            b6[a4 + 1] = np.sign(b6[a4 + 1]) * ((int(np.abs(b6[a4 + 1]) / 10) * 10) + int(np.abs(b28) % 10))
            b28 = int(b28 / 10)
            b7[a4] = np.sign(b7[a4]) * ((int(np.abs(b7[a4]) / 10) * 10) + int(np.abs(b28) % 10))
            a4 += b27
            a5 += 1
        b29 = np.column_stack((b6, b7)).astype(np.int16)
        wavfile.write(b13, rate1, b29)
    else:
        print('Your carrier should be min 6x longer than your message for this kind of steganography')
def fonk7():
    b30 = argparse.ArgumentParser()
    b30.add_argument("INPUT1", b31 = "Name of the wave file")
    b30.add_argument("INPUT2", b31 = "Name of the wave or txt file")
    b30.add_argument("-t", "--text", b31 = "Input text.", action='store_true')
    b30.add_argument("-s", "--sound", b31 = "Input sound for AM modulation.", action='store_true')
    b30.add_argument("-c", "--sCrypto", b31 = "Input sound for crypto-steganography.", action='store_true')
    b30.add_argument("-o", "--b36", b31 = "Name of the b36 wav file. Default value: out.wav).")
    b32 = b30.parse_args()
    b33 = True
    b34 = False
    b35 = False
    b36 = "out.wav"
    b37 = "Text"
    a6 = 0
    if b32.text:
        b33 = b32.text
        a6 += 1
    if b32.sound:
        b34 = b32.sound
        b37 = "Sound"
        a6 += 1
        b33 = False
    if b32.sCrypto:
        b35 = b32.sCrypto
        b37 = "Crypto"
        a6 += 1
        b33 = False
    if b32.b36:
        b36 = b32.b36
    print('Input file1: %s' % b32.INPUT1)
    print('Input file2: %s' % b32.INPUT2)
    print('Operation: %s' % b37)
    print('Output: %s' % b36)
    if a6 != 1:
        print('Error: Exactly one b37 should be selected!')
        b33 = b34 = b35 = False
    return (b32.INPUT1, b32.INPUT2, b36, b33, b34, b35)
def fonk8():
    b32 = fonk7()
    if b32[3]:
        fonk4(b32[0], b32[1], b32[2])
    elif b32[4]:
        fonk3(b32[1], True)
        fonk3(b32[0], False)
        fonk5(b32[0], b32[1], b32[2])
    elif b32[5]:
        fonk3(b32[1], False)
        fonk6(b32[0], b32[1], b32[2])
if b38 = = '__main__':
    fonk8()