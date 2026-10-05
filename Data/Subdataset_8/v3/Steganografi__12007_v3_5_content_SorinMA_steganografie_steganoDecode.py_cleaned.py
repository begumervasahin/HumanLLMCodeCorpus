import argparse
import numpy as np
import math
from numpy import fft
import wave
import struct
from scipy.io import wavfile
SAMPLE_RATE = 44100
NYQUIST_RATE = SAMPLE_RATE / 2.0
FFT_LENGTH = 512
def lowpass_coefs(cutoff):
    cutoff /= (NYQUIST_RATE / (FFT_LENGTH / 2.0))
    mask = [1.0 if f <= cutoff else 0.0 for f in range(FFT_LENGTH
    mask += mask[:0:-1]
    impulse_response = fft.ifft(mask).real.tolist()
    b = FFT_LENGTH
    for n in range(b):
        impulse_response[n] *= (n + 0.0) / b
    for n in range(b + 1, FFT_LENGTH):
        impulse_response[n] *= (FFT_LENGTH - n + 0.0) / b
    return impulse_response
def lowpass(original, cutoff):
    coefs = lowpass_coefs(cutoff)
    return np.convolve(original, coefs)
def stegoMod1(input_file, output_file):
    with wave.open(input_file, mode='rb') as song:
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    decoded = string.split("\0")[0]
    with open(output_file, "w") as text_file:
        text_file.write(decoded)
def stegoMod2(input_file, output_file):
    with wave.open(input_file, "rb") as modulated, wave.open(output_file, "wb") as demod_amsc_ok:
        demod_amsc_ok.setnchannels(1)
        demod_amsc_ok.setsampwidth(2)
        demod_amsc_ok.setframerate(44100)
        for _ in range(modulated.getnframes()):
            signal = struct.unpack('h', modulated.readframes(1))[0] / 32768.0
            carrier = math.cos(22050.0 * (n / 44100.0) * math.pi * 2)
            base = signal * carrier
            demod_amsc_ok.writeframes(struct.pack('h', int(base * 32767)))
def stegoMod2_2(output_file):
    rate, audio = wavfile.read(output_file)
    audio = 8 * lowpass(1 / 2 * audio, 4500)
    audio = audio.astype(np.int16)
    wavfile.write(output_file, rate, audio)
def stegoMod3(input_file, output_file):
    rate, audio = wavfile.read(input_file)
    left = audio[...,0].copy()
    right = audio[...,1].copy()
    a1, a2 = right[0], right[1]
    a = a1 * 1000 + a2
    frame = np.array([])
    add = int((len(left) / a - 1))
    contor = 4
    index = 0
    narray = []
    while index < a:
        aux = int(np.abs(right[contor]) % 10)
        aux = aux * 10 + int(np.abs(left[contor + 1]) % 10)
        aux = aux * 10 + int(np.abs(right[contor + 2]) % 10)
        aux = aux * 10 + int(np.abs(left[contor + 3]) % 10)
        aux = aux * 10 + int(np.abs(right[contor + 4]) % 10)
        signA = int(np.abs(left[contor + 5]) % 10)
        aux *= (signA - 1)
        narray.append(aux)
        contor += add
        index += 1
    frame = np.append(frame, narray)
    wavfile.write(output_file, rate, (frame.T).astype(np.int16))
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT_FILE", help="Input wave file")
    parser.add_argument("-t", "--text", help="Extract text from audio", action='store_true')
    parser.add_argument("-s", "--sound", help="Demodulate AM signal", action='store_true')
    parser.add_argument("-c", "--crypto", help="Perform steganography method 3", action='store_true')
    parser.add_argument("-o", "--output", help="Output wav file. Default: out.wav")
    return parser.parse_args()
if __name__ == '__main__':
    args = parse_arguments()
    if args.text:
        stegoMod1(args.INPUT_FILE, args.output)
    elif args.sound:
        stegoMod2(args.INPUT_FILE, args.output)
        stegoMod2_2(args.output)
    elif args.crypto:
        stegoMod3(args.INPUT_FILE, args.output)
    else:
        print("Error: Please specify an operation to perform.")