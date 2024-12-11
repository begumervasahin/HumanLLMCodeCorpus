import tkinter as tk
from easygui import fileopenbox
from scipy.io import wavfile
import numpy as np
import wave
import struct
import math
from scipy.fftpack import fft
import matplotlib.pyplot as plt
b33 = 44100
b34 = b33 / 2.0
b38 = 512
def fonk1(b24, b39 = 0, b6=0):
    b24 /= (b34 / (b38 / 2.0))
    b39 /= (b34 / (b38 / 2.0))
    b44 = []
    b4 = []
    b5 = b38
    for f in range(0, b5+1):
        b43 = 1.0
        if not b6:
            if f > b24:
                b43 = 0
        elif b6 = = 1:
            if f < b24:
                b43 = 0
        else:
            if f < b24 or f > b39:
                b43 = 0
        b44.append(b43)
        if f > 0 and f < b5:
            b4.append(b43)
    b4.reverse()
    b44 = b44 + b4
    b7 = np.fft.ifft(b44).real.tolist()
    b8 = b7[:b38
    b9 = b7[b38
    b7 = b9 + b8
    b10 = b38
    for n in range(0, b10):
        b7[n] *= (n + 0.0) / b10
    for n in range(b10 + 1, b38):
        b7[n] *= (b38 - n + 0.0) / b10
    return b7
def fonk2(original, cutoff):
    b11 = fonk1(b24=cutoff, b6=0)
    return np.convolve(original, b11)
def fonk3(input_file, apply_filter):
    rate, b12 = wavfile.read(input_file)
    try:
        b13 = len(b12[0])
        b14 = np.mean(b12, axis=1)
        if apply_filter:
            b14 = 2 * fonk2(0.5 * b14, 4500)
        wavfile.write(input_file + 'aux.wav', rate, b14.astype(np.int16))
        print('Step - ok')
    except:
        if apply_filter:
            b12 = 2 * fonk2(0.5 * b12, 4500)
        wavfile.write(input_file + 'aux.wav', rate, b12.astype(np.int16))
        print('Step - ok but exception')
def fonk4(input_file1, input_file2, output_file):
    b15 = wave.open(input_file1 + 'aux.wav', "r")
    b16 = wave.open(input_file2 + 'aux.wav', "r")
    b17 = wave.open(output_file, "w")
    for f in [b17]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    a4 = 0
    for n in range(0, b15.getnframes()):
        b18 = (struct.unpack('h', b15.readframes(1))[0] / 32768.0) / 2
        if a4 < b16.getnframes():
            b19 = struct.unpack('h', b16.readframes(1))[0] / 32768.0
            b20 = math.cos(22050.0 * (a4 / 44100.0) * math.pi * 2)
            b18 += b19 * b20 / 4
            a4 += 1
        b17.writeframes(struct.pack('h', int(b18 * 32767)))
def fonk5(input_file1, input_file2, output_file):
    fonk3(input_file2, True)
    fonk3(input_file1, False)
    fonk4(input_file1, input_file2, output_file)
def fonk6(input_file, apply_filter, b21 = 0, b35=4500, b40=0):
    rate, b12 = wavfile.read(input_file)
    b22 = 'aux.wav'
    if b21 = = 0:
        b22 = '_L_' + b22
    elif b21 = = 2:
        b22 = '_M_' + b22
    else:
        b22 = '_H_' + b22
    try:
        b13 = len(b12[0])
        b14 = np.mean(b12, axis=1)
        if apply_filter:
            b14 = np.convolve(b14, fonk1(b24=b35, b39=b40, b6=b21))
        wavfile.write(input_file + b22, rate, b14.astype(np.int16))
        print('Step - ok')
    except:
        if apply_filter:
            b12 = np.convolve(b12, fonk1(b24=b35, b39=b40, b6=b21))
        wavfile.write(input_file + b22, rate, b12.astype(np.int16))
        print('Step - ok but exception')
def fonk7(input_file, b21 = 0, b35=4500, b40=0):
    rate, b12 = wavfile.read(input_file)
    b22 = 'aux.wav'
    if b21 = = 0:
        b22 = '_L_' + b22
    elif b21 = = 2:
        b22 = '_M_' + b22
    else:
        b22 = '_H_' + b22
    b23 = np.zeros((2 * len(b12[...,0]), len(b12[0])))
    for i in range(len(b12[0])):
        b23[...,i] = np.convolve(b12[...,i], fonk1(b24 = b35, b39=b40, b6=b21))[:len(b23[...,i])]
    wavfile.write(input_file + b22, rate, b23.astype(np.int16))
    print('Step - ok')
def fonk8(file_wav):
    fs, b25 = wavfile.read(file_wav)
    b26 = b25.T
    b10 = [(ele / 2 ** 8.) * 2 - 1 for ele in b26]
    b27 = fft(b10)
    b28 = len(b27) / 2
    plt.plot(abs(b27[:int(b28 - 1)]), 'r')
    plt.show()
    plt.plot(b10[:int(b28 - 1)], 'r')
    plt.show()
def fonk9(file_wav):
    fs, b25 = wavfile.read(file_wav)
    try:
        b26 = list(map(lambda x: x[0] + x[1], zip(b25.T[0], b25.T[1])))
    except:
        b26 = b25.T[0]
    b10 = [(ele / 2 ** 8.) * 2 - 1 for ele in b26]
    b27 = fft(b10)
    b28 = len(b27) / 2
    b29 = tk.Tk()
    b29.wm_title((file_wav.split('\\'))[-1])
    b30 = plt.figure(figsize=(5, 4), dpi=100)
    b31 = np.arange(0, 3, .01)
    b30.add_subplot(211).plot(abs(b27[:int(b28 - 1)]), 'r')
    b30.add_subplot(212).plot(b10[:int(b28 - 1)], 'r')
    plt.show()
def fonk10(file_wav):
    fs1, b32 = wavfile.read((file_wav.split('\\'))[-1] + '_L_aux.wav')
    b33 = b32.T
    b34 = [(ele / 2 ** 8.) * 2 - 1 for ele in b33]
    b35 = fft(b34)
    b36 = len(b35) / 2
    fs2, b37 = wavfile.read((file_wav.split('\\'))[-1] + '_M_aux.wav')
    b38 = b37.T
    b39 = [(ele / 2 ** 8.) * 2 - 1 for ele in b38]
    b40 = fft(b39)
    b41 = len(b40) / 2
    fs3, b42 = wavfile.read((file_wav.split('\\'))[-1] + '_H_aux.wav')
    b43 = b42.T
    b44 = [(ele / 2 ** 8.) * 2 - 1 for ele in b43]
    b45 = fft(b44)
    b46 = len(b45) / 2
    b29 = tk.Tk()
    b29.wm_title((file_wav.split('\\'))[-1] + 'Low_Mid_Hi')
    b30 = plt.figure(figsize=(5, 4), dpi=100)
    b31 = np.arange(0, 3, .01)
    b30.add_subplot(611).plot(abs(b35[:int(b36 - 1)]), 'r')
    b30.add_subplot(612).plot(b34[:int(b36 - 1)], 'r')
    b30.add_subplot(613).plot(abs(b40[:int(b41 - 1)]), 'r')
    b30.add_subplot(614).plot(b39[:int(b41 - 1)], 'r')
    b30.add_subplot(615).plot(abs(b45[:int(b46 - 1)]), 'r')
    b30.add_subplot(616).plot(b44[:int(b46 - 1)], 'r')
    plt.show()
def fonk11(file_wav, lr):
    b47 = 'Left'
    if lr:
        b47 = 'Right'
    fs1, b32 = wavfile.read((file_wav.split('\\'))[-1] + '_L_aux.wav')
    b33 = b32.T[lr]
    b34 = [(ele / 2 ** 8.) * 2 - 1 for ele in b33]
    b35 = fft(b34)
    b36 = len(b35) / 2
    fs2, b37 = wavfile.read((file_wav.split('\\'))[-1] + '_M_aux.wav')
    b38 = b37.T[lr]
    b39 = [(ele / 2 ** 8.) * 2 - 1 for ele in b38]
    b40 = fft(b39)
    b41 = len(b40) / 2
    fs3, b42 = wavfile.read((file_wav.split('\\'))[-1] + '_H_aux.wav')
    b43 = b42.T[lr]
    b44 = [(ele / 2 ** 8.) * 2 - 1 for ele in b43]
    b45 = fft(b44)
    b46 = len(b45) / 2
    b29 = tk.Tk()
    b29.wm_title(b47 + (file_wav.split('\\'))[-1] + 'Low_Mid_Hi' + b47)
    b30 = plt.figure(figsize=(5, 4), dpi=100)
    b31 = np.arange(0, 3, .01)
    b30.add_subplot(611).plot(abs(b35[:int(b36 - 1)]), 'r')
    b30.add_subplot(612).plot(b34[:int(b36 - 1)], 'r')
    b30.add_subplot(613).plot(abs(b40[:int(b41 - 1)]), 'r')
    b30.add_subplot(614).plot(b39[:int(b41 - 1)], 'r')
    b30.add_subplot(615).plot(abs(b45[:int(b46 - 1)]), 'r')
    b30.add_subplot(616).plot(b44[:int(b46 - 1)], 'r')
    plt.show()
def fonk12():
    global b48
    b48 = fileopenbox()
def fonk13():
    global b49
    b49 = fileopenbox()
def fonk14():
    global b48
    fonk9(b48)
def fonk15():
    global b49
    fonk9(b49)
def fonk16():
    global b48, b49
    fonk9(b48)
    fonk9(b49)
b29 = tk.Tk()
b50 = "MCT_MDO"
b29.title(b50)
b29.columnconfigure(0, b51 = 1)
b29.rowconfigure(0, b51 = 1)
b52 = [
    "Import Song 1",
    "Import Song 2",
    "Plot Song 1",
    "Plot Song 2",
    "Plot Both Songs"
]
tk.Label(b29, b53 = "Martinescu_Danoiu_Orbisor_343A3").grid(b55=0, column=0, columnspan=len(b52), stick="n", pady=(15,0))
b54 = tk.Frame(b29)
b54.grid(b55 = 2, column=0)
tk.Button(b54, b53 = b52[0], command=select_song1).grid(b55=0, column=0, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b54, b53 = b52[1], command=select_song2).grid(b55=0, column=1, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b54, b53 = b52[2], command=plot_song1).grid(b55=0, column=2, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b54, b53 = b52[3], command=plot_song2).grid(b55=0, column=3, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b54, b53 = b52[4], command=plot_both_songs).grid(b55=0, column=4, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b54, b53 = 'Exit', command=b29.destroy).grid(b55=0, column=5, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
b29.mainloop()