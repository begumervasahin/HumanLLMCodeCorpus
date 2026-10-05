import argparse
import math
import numpy as np
from numpy import fft
import struct
import wave
from scipy.io import wavfile
a1 = 44100
b1 = a1 / 2.0
a2 = 512
def fonk1(cutoff):
    cutoff /= (b1 / (a2 / 2.0))
    b2 = []
    b3 = []
    b4 = a2
    for f in range(0, b4+1):
        b5 = 1.0 if f <= cutoff else 0
        b2.append(b5)
        if 0 < f < b4:
            b3.append(b5)
    b3.reverse()
    b2 += b3
    b6 = fft.ifft(b2).real.tolist()
    b7 = b6[:a2
    b8 = b6[a2
    b6 = b8 + b7
    b9 = a2
    for n in range(0, b9):
        b6[n] *= (n + 0.0) / b9
    for n in range(b9 + 1, a2):
        b6[n] *= (a2 - n + 0.0) / b9
    return b6
def fonk2(original, cutoff):
    b10 = fonk1(cutoff)
    return np.convolve(original, b10)
def fonk3(b38, filtr):
    rate, b11 = wavfile.read(b38)
    try:
        b12 = len(b11[0])
        b13 = np.zeros(len(b11[...,0]))
        for i in range(b12):
            b13 += b11[...,i] / b12
        if filtr:
            b13 = 2 * fonk2(0.5 * b13, 4500)
        wavfile.write('b28' + b38, rate, b13.astype(np.int16))
        print('Step - ok')
    except:
        if filtr:
            b11 = 2 * fonk2(0.5 * b11, 4500)
        wavfile.write('b28' + b38, rate, b11.astype(np.int16))
        print('Step - ok but exception')
def fonk4(inpt1, inpt2, b36):
    b14 = wave.open(inpt1, mode='rb')
    b15 = bytearray(list(b14.readframes(b14.getnframes())))
    with open(inpt2, 'r') as file:
        b16 = file.read().replace('\n', '')
    b16 = b16 + '*' * int((len(b15) - len(b16) * 8 * 8) / 8)
    b17 = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in b16])))
    if len(b17) < b14.getnframes():
        for i, bit in enumerate(b17):
            b15[i] = (b15[i] & 254) | bit
        b18 = bytes(b15)
        with wave.open(b36, 'wb') as fd:
            fd.setparams(b14.getparams())
            fd.writeframes(b18)
        b14.close()
    else:
        print("Bits overflow for stegano, but we still put a piece of message in your b11 carrier!")
        a3 = 0
        for i, bit in enumerate(b17):
            if a3 < b14.getnframes():
                b15[i] = (b15[i] & 254) | bit
                a3 += 1
            else:
                break
        b18 = bytes(b15)
        with wave.open(b36, 'wb') as fd:
            fd.setparams(b14.getparams())
            fd.writeframes(b18)
        b14.close()
def fonk5(inpt1, inpt2, b36):
    b19 = wave.open('b28' + inpt1, "r")
    b20 = wave.open('b28' + inpt2, "r")
    b21 = wave.open(b36, "w")
    for f in [b21]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    a3 = 0
    for n in range(0, b19.getnframes()):
        b22 = (struct.unpack('h', b19.readframes(1))[0] / 32768.0) / 2
        if a3 < b20.getnframes():
            b23 = struct.unpack('h', b20.readframes(1))[0] / 32768.0
            b24 = math.cos(22050.0 * (a3 / 44100.0) * math.pi * 2)
            b22 += b23 * b24 / 4
            a3 += 1
        b21.writeframes(struct.pack('h', int(b22 * 32767)))
def fonk6(inpt1, inpt2, b36):
    rate1, b25 = wavfile.read(inpt1)
    rate2, b26 = wavfile.read('b28' + inpt2)
    b7 = b25[...,0].copy()
    b8 = b25[...,1].copy()
    b7[0] = b8[0] = len(b26) / 1000.0
    b7[1] = b8[1] = len(b26) % 1000.0
    a3 = 4
    b27 = int(len(b7) / len(b26) - 1)
    if b27 >= 6:
        print("OK")
        a4 = 0
        while a4 < len(b26):
            b28 = int(np.abs(b26[a4]))
            b7[a3 + 5] = np.sign(b7[a3+5])*((int(np.abs(b7[a3+5])/10)*10)  + 1+ np.sign(b26[a4]))
            b8[a3 + 4] = np.sign(b8[a3+4])*((int(np.abs(b8[a3+4])/10)*10) + int(np.abs(b28) % 10))
            b28 = int(b28/10)
            b7[a3 + 3] =  np.sign(b7[a3+3])*((int(np.abs(b7[a3+3])/10)*10) + int(np.abs(b28) % 10))
            b28 = int(b28/10)
            b8[a3 + 2] =  np.sign(b8[a3+2])*((int(np.abs(b8[a3+2])/10)*10) + int(np.abs(b28) % 10))
            b28 = int(b28/10)
            b7[a3 + 1] =  np.sign(b7[a3+1])*((int(np.abs(b7[a3+1])/10)*10) + int(np.abs(b28) % 10))
            b28 = int(b28/10)
            b8[a3] =  np.sign(b8[a3])*((int(np.abs(b8[a3])/10)*10) + int(np.abs(b28) % 10))
            a3 += b27
            a4 += 1
        b29 = np.column_stack((b7, b8)).astype(np.int16)
        wavfile.write(b36, rate1, b29)
    else:
        print('Your carrier should be at least 6 times longer than your message for this kind of stegano')
def fonk7():
    b30 = argparse.ArgumentParser()
    b30.add_argument("INPUT1", b31 = "Name of the wave file")
    b30.add_argument("INPUT2", b31 = "Name of the wave or txt file")
    b30.add_argument("-t", "--b33", b31 = "Input b33.", action='store_true')
    b30.add_argument("-s", "--b34", b31 = "Input b34 for AM modulation.", action='store_true')
    b30.add_argument("-c", "--b35", b31 = "Input b34 for crypto-stegano.", action='store_true')
    b30.add_argument("-o", "--b36", b31 = "Name of the b36 wav file. Default value: out.wav).")
    b32 = b30.fonk7()
    b33 = b32.b33
    b34 = b32.b34
    b35 = b32.b35
    b36 = b32.b36 if b32.b36 else "out.wav"
    b37 = "Text" if b32.b33 else ("Sound" if b32.b34 else "Crypto")
    print('Input file1: %s' % b32.INPUT1)
    print('Input file2: %s' % b32.INPUT2)
    print('Operation: %s' % b37)
    print('Output: %s' % b36)
    if sum([b32.b33, b32.b34, b32.b35]) != 1:
        print('Error: More than 1 b37 selected!')
        b33 = b34 = b35 = False
    return (b32.INPUT1, b32.INPUT2, b36, b33, b34, b35)
def fonk8():
    b38 = fonk7()
    if b38[3]:
        mod1(b38[0], b38[1], b38[2])
    if b38[4]:
        mod2(b38[0], b38[1], b38[2])
    if b38[5]:
        mod3(b38[0], b38[1], b38[2])
if b39 = = '__main__':
    fonk8()