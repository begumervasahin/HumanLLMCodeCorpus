import argparse
import numpy as np
import wave
import struct
import math
from numpy import fft
from scipy.io import wavfile
b20 = 44100
b1 = b20 / 2.0
b21 = 512
def fonk1(cutoff):
    cutoff /= (b1 / (b21 / 2.0))
    b2 = [1.0 if f <= cutoff else 0 for f in range(0, b21
    b2 += b2[::-1][1:]
    b3 = fft.ifft(b2).real.tolist()
    b4 = b21
    for n in range(0, b4):
        b3[n] *= (n + 0.0) / b4
    for n in range(b4 + 1, b21):
        b3[n] *= (b21 - n + 0.0) / b4
    return b3
def fonk2(original, cutoff):
    b5 = fonk1(cutoff)
    return np.convolve(original, b5)
def fonk3(input_file, output_file):
    b6 = wave.open(input_file, mode='rb')
    b7 = bytearray(list(b6.readframes(b6.getnframes())))
    b8 = [b7[i] & 1 for i in range(len(b7))]
    b9 = "".join(chr(int("".join(map(str, b8[i:i+8])), 2)) for i in range(0, len(b8), 8))
    b10 = b9.split("\0")
    with open(output_file, "w") as text_file:
        text_file.write(b10)
    b6.close()
def fonk4(input_file, output_file):
    b11 = wave.open(input_file, "r")
    b12 = wave.open(output_file, "w")
    for f in [b12]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    for n in range(0, b11.getnframes()):
        b13 = struct.unpack('h', b11.readframes(1))[0] / 32768.0
        b14 = math.cos(22050.0 * (n / 44100.0) * math.pi * 2)
        b15 = b13 * b14
        b12.writeframes(struct.pack('h', int(b15 * 32767)))
def fonk5(output_file):
    rate1, b16 = wavfile.read(output_file)
    b16 = 8 * fonk2(1 / 2 * b16, 4500)
    b17 = b16.astype(np.int16)
    wavfile.write(output_file, rate1, b17)
def fonk6(input_file, output_file):
    rate1, b16 = wavfile.read(input_file)
    b18 = b16[..., 0].copy()
    b19 = b16[..., 1].copy()
    b20 = b19[0]
    b21 = b19[1]
    b22 = b20 * 1000 + b21
    b23 = np.array([])
    b24 = int((len(b18) / b22 - 1))
    a3 = 4
    a4 = 0
    b25 = []
    while a4 < b22:
        a5 = 0
        a5 += int(np.abs(b19[a3]) % 10)
        a5 = a5 * 10 + int(np.abs(b18[a3 + 1]) % 10)
        a5 = a5 * 10 + int(np.abs(b19[a3 + 2]) % 10)
        a5 = a5 * 10 + int(np.abs(b18[a3 + 3]) % 10)
        a5 = a5 * 10 + int(np.abs(b19[a3 + 4]) % 10)
        b26 = int(np.abs(b18[a3 + 5]) % 10)
        a5 = a5 * (b26 - 1)
        b25.append(a5)
        a3 += b24
        a4 += 1
    b23 = np.append(b23, b25)
    wavfile.write(output_file, rate1, (b23.T).astype(np.int16))
def fonk7():
    b27 = argparse.ArgumentParser()
    b27.add_argument("INPUT1", b28 = "Name of the wave file")
    b27.add_argument("-t", "--b30", b28 = "Input b30.", action='store_true')
    b27.add_argument("-s", "--b31", b28 = "Input b31 for AM modulation.", action='store_true')
    b27.add_argument("-c", "--b32", b28 = "Input b31 for cypto-stegano.", action='store_true')
    b27.add_argument("-o", "--b33", b28 = "Name of the b33 wav file. Default value: out.wav).")
    b29 = b27.parse_args()
    b30 = True
    b31 = False
    b32 = False
    b33 = "out.wav"
    b34 = "Text"
    a3 = 0
    if b29.b30:
        b30 = b29.b30
        a3 += 1
    if b29.b31:
        b31 = b29.b31
        b34 = "Sound"
        a3 += 1
        b30 = False
    if b29.b32:
        b32 = b29.b32
        b34 = "Crypto"
        a3 += 1
        b30 = False
    if b29.b33:
        b33 = b29.b33
    print('Input file1: %s' % b29.INPUT1)
    print('Operation: %s' % b34)
    print('Output: %s' % b33)
    if a3 > 1:
        print('Error, more than just 1 b34 selected!')
        b30 = b31 = b32 = False
    return (b29.INPUT1, b33, b30, b31, b32)
def fonk8(input_file, output_file, b30, b31, b32):
    if b30:
        fonk3(input_file, output_file)
    if b31:
        fonk4(input_file, output_file)
        fonk5(output_file)
    if b32:
        fonk6(input_file, output_file)
if b35 = = '__main__':
    b36 = fonk7()
    fonk8(*b36)