import argparse
import math
import struct
import wave
from scipy.io import wavfile
import numpy as np
from numpy import fft
SAMPLE_RATE = 44100
NYQUIST_RATE = SAMPLE_RATE / 2.0
FFT_LENGTH = 512
def lowpass_coefs(cutoff):
    cutoff /= (NYQUIST_RATE / (FFT_LENGTH / 2.0))
    mask = []
    negatives = []
    l = FFT_LENGTH
    for f in range(0, l + 1):
        rampdown = 1.0
        if f > cutoff:
            rampdown = 0
        mask.append(rampdown)
        if 0 < f < l:
            negatives.append(rampdown)
    negatives.reverse()
    mask = mask + negatives
    impulse_response = fft.ifft(mask).real.tolist()
    left = impulse_response[:FFT_LENGTH
    right = impulse_response[FFT_LENGTH
    impulse_response = right + left
    b = FFT_LENGTH
    for n in range(0, b):
        impulse_response[n] *= (n + 0.0) / b
    for n in range(b + 1, FFT_LENGTH):
        impulse_response[n] *= (FFT_LENGTH - n + 0.0) / b
    return impulse_response
def lowpass(original, cutoff):
    coefs = lowpass_coefs(cutoff)
    return np.convolve(original, coefs)
def fromNto1Ch(inpt, filter_flag):
    rate, audio = wavfile.read(inpt)
    try:
        nrOfChannels = len(audio[0])
        monoChFrame = np.array([0] * len(audio[..., 0])).astype(np.float)
        for i in range(nrOfChannels):
            monoChFrame += 1 / nrOfChannels * audio[..., i].astype(np.float)
        if filter_flag:
            monoChFrame = 2 * lowpass(1 / 2 * monoChFrame, 4500)
        wavfile.write('aux' + inpt, rate, monoChFrame.astype(np.int16))
        print('Step - Successful')
    except Exception as e:
        print(f'Exception occurred: {e}')
        if filter_flag:
            audio = 2 * lowpass(1 / 2 * audio, 4500)
        wavfile.write('aux' + inpt, rate, audio.astype(np.int16))
        print('Step - Successful, but encountered exception')
def stegoMod1(inpt1, inpt2, output):
    song = wave.open(inpt1, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    with open(inpt2, 'r') as file:
        string = file.read().replace('\n', '')
    string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * ' '
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
    if len(bits) < song.getnframes():
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        frame_modified = bytes(frame_bytes)
        with wave.open(output, 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)
        song.close()
    else:
        print("Bits overflow for steganography, but still embedding part of the message in your audio carrier!")
        contor = 0
        for i, bit in enumerate(bits):
            if contor < song.getnframes():
                frame_bytes[i] = (frame_bytes[i] & 254) | bit
                contor += 1
            else:
                break
        frame_modified = bytes(frame_bytes)
        with wave.open(output, 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)
        song.close()
def stegoMod2(inpt1, inpt2, output):
    baseband1 = wave.open('aux' + inpt1, "r")
    baseband2 = wave.open('aux' + inpt2, "r")
    amsc = wave.open(output, "w")
    for f in [amsc]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    contor = 0
    for n in range(0, baseband1.getnframes()):
        base = (struct.unpack('h', baseband1.readframes(1))[0] / 32768.0) / 2
        if contor < baseband2.getnframes():
            encodFrame = struct.unpack('h', baseband2.readframes(1))[0] / 32768.0
            carrier_sample = math.cos(22050.0 * (contor / 44100.0) * math.pi * 2)
            base += encodFrame * carrier_sample / 4
            contor += 1
        amsc.writeframes(struct.pack('h', int(base * 32767)))
def stegoMod3(inpt1, inpt2, output):
    rate1, audio1 = wavfile.read(inpt1)
    rate2, audio2 = wavfile.read('aux' + inpt2)
    left = audio1[..., 0].copy()
    right = audio1[..., 1].copy()
    left[0] = right[0] = len(audio2) / 1000.0
    left[1] = right[1] = len(audio2) % 1000.0
    contor = 4
    add = int((len(left) / len(audio2) - 1))
    if add >= 6:
        print("OK")
        index = 0
        while index < len(audio2):
            aux = int(np.abs(audio2[index]))
            left[contor + 5] = np.sign(left[contor + 5]) * (
                    (int(np.abs(left[contor + 5]) / 10) * 10) + 1 + np.sign(audio2[index]))
            right[contor + 4] = np.sign(right[contor + 4]) * (
                    (int(np.abs(right[contor + 4]) / 10) * 10) + int(np.abs(aux) % 10))
            aux = int(aux / 10)
            left[contor + 3] = np.sign(left[contor + 3]) * (
                    (int(np.abs(left[contor + 3]) / 10) * 10) + int(np.abs(aux) % 10))
            aux = int(aux / 10)
            right[contor + 2] = np.sign(right[contor + 2]) * (
                    (int(np.abs(right[contor + 2]) / 10) * 10) + int(np.abs(aux) % 10))
            aux = int(aux / 10)
            left[contor + 1] = np.sign(left[contor + 1]) * (
                    (int(np.abs(left[contor + 1]) / 10) * 10) + int(np.abs(aux) % 10))
            aux = int(aux / 10)
            right[contor] = np.sign(right[contor]) * (
                    (int(np.abs(right[contor]) / 10) * 10) + int(np.abs(aux) % 10))
            contor += add
            index += 1
        audiox = np.column_stack((left, right)).astype(np.int16)
        wavfile.write(output, rate1, audiox)
    else:
        print('Your carrier should be min 6x longer than your message for this kind of steganography')
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT1", help="Name of the wave file")
    parser.add_argument("INPUT2", help="Name of the wave or txt file")
    parser.add_argument("-t", "--text", help="Input text.", action='store_true')
    parser.add_argument("-s", "--sound", help="Input sound for AM modulation.", action='store_true')
    parser.add_argument("-c", "--sCrypto", help="Input sound for crypto-steganography.", action='store_true')
    parser.add_argument("-o", "--output", help="Name of the output wav file. Default value: out.wav).")
    args = parser.parse_args()
    text_flag = True
    sound_flag = False
    sCrypto_flag = False
    output = "out.wav"
    operation = "Text"
    count = 0
    if args.text:
        text_flag = args.text
        count += 1
    if args.sound:
        sound_flag = args.sound
        operation = "Sound"
        count += 1
        text_flag = False
    if args.sCrypto:
        sCrypto_flag = args.sCrypto
        operation = "Crypto"
        count += 1
        text_flag = False
    if args.output:
        output = args.output
    print('Input file1: %s' % args.INPUT1)
    print('Input file2: %s' % args.INPUT2)
    print('Operation: %s' % operation)
    print('Output: %s' % output)
    if count != 1:
        print('Error: Exactly one operation should be selected!')
        text_flag = sound_flag = sCrypto_flag = False
    return (args.INPUT1, args.INPUT2, output, text_flag, sound_flag, sCrypto_flag)
def main():
    args = parse_arguments()
    if args[3]:
        stegoMod1(args[0], args[1], args[2])
    elif args[4]:
        fromNto1Ch(args[1], True)
        fromNto1Ch(args[0], False)
        stegoMod2(args[0], args[1], args[2])
    elif args[5]:
        fromNto1Ch(args[1], False)
        stegoMod3(args[0], args[1], args[2])
if __name__ == '__main__':
    main()