import argparse
import numpy as np
import math
from numpy import fft
import wave
import struct
from scipy.io import wavfile
a1 = 44100
b1 = a1 / 2.0
b17 = 512
def fonk1(cutoff):
    cutoff /= (b1 / (b17 / 2.0))
    b2 = [1.0 if f <= cutoff else 0.0 for f in range(b17
    b2 += b2[:0:-1]
    b3 = fft.ifft(b2).real.tolist()
    b4 = b17
    for n in range(b4):
        b3[n] *= (n + 0.0) / b4
    for n in range(b4 + 1, b17):
        b3[n] *= (b17 - n + 0.0) / b4
    return b3
def fonk2(original, cutoff):
    b5 = fonk1(cutoff)
    return np.convolve(original, b5)
def fonk3(input_file, output_file):
    with wave.open(input_file, b6 = 'rb') as song:
        b7 = bytearray(list(song.readframes(song.getnframes())))
    b8 = [b7[i] & 1 for i in range(len(b7))]
    b9 = "".join(chr(int("".join(map(str, b8[i:i+8])), 2)) for i in range(0, len(b8), 8))
    b10 = b9.split("\0")[0]
    with open(output_file, "w") as text_file:
        text_file.write(b10)
def fonk4(input_file, output_file):
    with wave.open(input_file, "rb") as modulated, wave.open(output_file, "wb") as demod_amsc_ok:
        demod_amsc_ok.setnchannels(1)
        demod_amsc_ok.setsampwidth(2)
        demod_amsc_ok.setframerate(44100)
        for _ in range(modulated.getnframes()):
            b11 = struct.unpack('h', modulated.readframes(1))[0] / 32768.0
            b12 = math.cos(22050.0 * (n / 44100.0) * math.pi * 2)
            b13 = b11 * b12
            demod_amsc_ok.writeframes(struct.pack('h', int(b13 * 32767)))
def fonk5(output_file):
    rate, b14 = wavfile.read(output_file)
    b14 = 8 * fonk2(1 / 2 * b14, 4500)
    b14 = b14.astype(np.int16)
    wavfile.write(output_file, rate, b14)
def fonk6(input_file, output_file):
    rate, b14 = wavfile.read(input_file)
    b15 = b14[...,0].copy()
    b16 = b14[...,1].copy()
    a1, b17 = b16[0], b16[1]
    b18 = a1 * 1000 + b17
    b19 = np.array([])
    b20 = int((len(b15) / b18 - 1))
    a3 = 4
    a4 = 0
    b21 = []
    while a4 < b18:
        b22 = int(np.abs(b16[a3]) % 10)
        b22 = b22 * 10 + int(np.abs(b15[a3 + 1]) % 10)
        b22 = b22 * 10 + int(np.abs(b16[a3 + 2]) % 10)
        b22 = b22 * 10 + int(np.abs(b15[a3 + 3]) % 10)
        b22 = b22 * 10 + int(np.abs(b16[a3 + 4]) % 10)
        b23 = int(np.abs(b15[a3 + 5]) % 10)
        b22 *= (b23 - 1)
        b21.append(b22)
        a3 += b20
        a4 += 1
    b19 = np.append(b19, b21)
    wavfile.write(output_file, rate, (b19.T).astype(np.int16))
def fonk7():
    b24 = argparse.ArgumentParser()
    b24.add_argument("INPUT_FILE", b25 = "Input wave file")
    b24.add_argument("-t", "--text", b25 = "Extract text from b14", action='store_true')
    b24.add_argument("-s", "--sound", b25 = "Demodulate AM b11", action='store_true')
    b24.add_argument("-c", "--crypto", b25 = "Perform steganography method 3", action='store_true')
    b24.add_argument("-o", "--output", b25 = "Output wav file. Default: out.wav")
    return b24.parse_args()
if b26 = = '__main__':
    b27 = fonk7()
    if b27.text:
        fonk3(b27.INPUT_FILE, b27.output)
    elif b27.sound:
        fonk4(b27.INPUT_FILE, b27.output)
        fonk5(b27.output)
    elif b27.crypto:
        fonk6(b27.INPUT_FILE, b27.output)
    else:
        print("Error: Please specify an operation to perform.")