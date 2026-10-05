import tkinter as tk
from tkinter import filedialog
import numpy as np
import wave
import struct
import math
from scipy.io import wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os
b36 = 44100
b37 = b36 / 2.0
b41 = 512
def fonk1(b24, b42 = 0, b6=0):
    b24 /= (b37 / (b41 / 2.0))
    b42 /= (b37 / (b41 / 2.0))
    b47 = []
    b4 = []
    b5 = b41
    for f in range(0, b5+1):
        b46 = 1.0
        if not b6:
            if f > b24:
                b46 = 0
        elif b6 = = 1:
            if f < b24:
                b46 = 0
        else:
            if f < b24 or f > b42:
                b46 = 0
        b47.append(b46)
        if f > 0 and f < b5:
            b4.append(b46)
    b4.reverse()
    b47 = b47 + b4
    b7 = np.fft.ifft(b47).real.tolist()
    b8 = b7[:b41
    b9 = b7[b41
    b7 = b9 + b8
    b10 = b41
    for n in range(0, b10):
        b7[n] *= (n + 0.0) / b10
    for n in range(b10 + 1, b41):
        b7[n] *= (b41 - n + 0.0) / b10
    return b7
def fonk2(original, cutoff):
    b11 = fonk1(b24=cutoff, b6=0)
    return np.convolve(original, b11)
def fonk3(inpt, filter_audio):
    rate, b12 = wavfile.read(inpt)
    try:
        b13 = len(b12[0])
        b14 = np.sum(b12, axis=1) / b13
        if filter_audio:
            b14 = 2 * fonk2(0.5 * b14, 4500)
        wavfile.write(inpt + 'aux.wav', rate, b14.astype(np.int16))
        print('Step - ok')
    except:
        if filter_audio:
            b12 = 2 * fonk2(0.5 * b12, 4500)
        wavfile.write(inpt + 'aux.wav', rate, b12.astype(np.int16))
        print('Step - ok but exception')
def fonk4(inpt1, inpt2, output):
    b15 = wave.open(inpt1 + 'aux.wav', "r")
    b16 = wave.open(inpt2 + 'aux.wav', "r")
    b17 = wave.open(output, "w")
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
def fonk5(inpt1, inpt2, output):
    fonk3(inpt2, True)
    fonk3(inpt1, False)
    fonk4(inpt1, inpt2, output)
def fonk6(inpt, filter_audio, b21 = 0, b38=4500, b43=0):
    rate, b12 = wavfile.read(inpt)
    b22 = 'aux.wav'
    if b21 = = 0:
        b22 = '_L_' + b22
    elif b21 = = 2:
        b22 = '_M_' + b22
    else:
        b22 = '_H_' + b22
    try:
        b13 = len(b12[0])
        b14 = np.sum(b12, axis=1) / b13
        if filter_audio:
            b14 = np.convolve(b14, fonk1(b24=b38, b42=b43, b6=b21))
        wavfile.write(inpt + b22, rate, b14.astype(np.int16))
        print('Step - ok')
    except:
        if filter_audio:
            b12 = np.convolve(b12, fonk1(b24=b38, b42=b43, b6=b21))
        wavfile.write(inpt + b22, rate, b12.astype(np.int16))
        print('Step - ok but exception')
def fonk7(inpt, b21 = 0, b38=4500, b43=0):
    rate, b12 = wavfile.read(inpt)
    b22 = 'aux.wav'
    if b21 = = 0:
        b22 = '_L_' + b22
    elif b21 = = 2:
        b22 = '_M_' + b22
    else:
        b22 = '_H_' + b22
    b23 = np.zeros((len(b12[...,0]) * 2, len(b12[0])))
    for i in range(len(b12[0])):
        b23[...,i] = np.convolve(b12[...,i], fonk1(b24 = b38, b42=b43, b6=b21))[:len(b23[...,i])]
    wavfile.write(inpt + b22, rate, b23.astype(np.int16))
    print('Step - ok')
def fonk8(file_wav):
    fs, b25 = wavfile.read(file_wav)
    b26 = b25.T
    b10 = [(ele / 2**8.) * 2 - 1 for ele in b26]
    b27 = fft(b10)
    b28 = len(b27) / 2
    plt.plot(abs(b27[:int(b28 - 1)]), 'r')
    plt.show()
    plt.plot(b10[:int(b28 - 1)], 'r')
    plt.show()
def fonk9(file_wav):
    fs, b25 = wavfile.read(file_wav)
    try:
        b26 = np.sum(b25.T, axis=0)
    except:
        b26 = b25.T[0]
    b10 = [(ele / 2**8.) * 2 - 1 for ele in b26]
    b27 = fft(b10)
    b28 = len(b27) / 2
    b29 = tk.Tk()
    b29.wm_title((file_wav.split('\\'))[-1])
    b30 = plt.figure(figsize=(5, 4), dpi=100)
    b30.add_subplot(211).plot(abs(b27[:int(b28 - 1)]), 'r')
    b30.add_subplot(212).plot(b10[:int(b28 - 1)], 'r')
    b31 = FigureCanvasTkAgg(b30, master=b29)
    b31.draw()
    b31.get_tk_widget().pack(b32 = tk.TOP, fill=tk.BOTH, expand=1)
    b33 = NavigationToolbar2Tk(b31, b29)
    b33.update()
    b31.get_tk_widget().pack(b32 = tk.TOP, fill=tk.BOTH, expand=1)
    def fonk10(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, b31, b33)
    b31.mpl_connect("key_press_event", on_key_press)
    def fonk11():
        b29.quit()
        b29.destroy()
    b34 = tk.Button(master=b29, text="Quit", command=_quit)
    b34.pack(b32 = tk.BOTTOM)
    tk.mainloop()
def fonk12(file_wav):
    fs1, b35 = wavfile.read((file_wav.split('\\'))[-1] + '_L_aux.wav')
    b36 = b35.T
    b37 = [(ele / 2**8.) * 2 - 1 for ele in b36]
    b38 = fft(b37)
    b39 = len(b38) / 2
    fs2, b40 = wavfile.read((file_wav.split('\\'))[-1] + '_M_aux.wav')
    b41 = b40.T
    b42 = [(ele / 2**8.) * 2 - 1 for ele in b41]
    b43 = fft(b42)
    b44 = len(b43) / 2
    fs3, b45 = wavfile.read((file_wav.split('\\'))[-1] + '_H_aux.wav')
    b46 = b45.T
    b47 = [(ele / 2**8.) * 2 - 1 for ele in b46]
    b48 = fft(b47)
    b49 = len(b48) / 2
    b29 = tk.Tk()
    b29.wm_title((file_wav.split('\\'))[-1] + 'Low_Mid_Hi')
    b30 = plt.figure(figsize=(5, 4), dpi=100)
    b30.add_subplot(611).plot(abs(b38[:int(b39 - 1)]), 'r')
    b30.add_subplot(612).plot(b37[:int(b39 - 1)], 'r')
    b30.add_subplot(613).plot(abs(b43[:int(b44 - 1)]), 'r')
    b30.add_subplot(614).plot(b42[:int(b44 - 1)], 'r')
    b30.add_subplot(615).plot(abs(b48[:int(b49 - 1)]), 'r')
    b30.add_subplot(616).plot(b47[:int(b49 - 1)], 'r')
    b31 = FigureCanvasTkAgg(b30, master=b29)
    b31.draw()
    b31.get_tk_widget().pack(b32 = tk.TOP, fill=tk.BOTH, expand=1)
    b33 = NavigationToolbar2Tk(b31, b29)
    b33.update()
    b31.get_tk_widget().pack(b32 = tk.TOP, fill=tk.BOTH, expand=1)
    def fonk13(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, b31, b33)
    b31.mpl_connect("key_press_event", on_key_press)
    def fonk14():
        b29.quit()
        b29.destroy()
    b34 = tk.Button(master=b29, text="Quit", command=_quit)
    b34.pack(b32 = tk.BOTTOM)
    tk.mainloop()
def fonk15(file_wav, lr):
    b50 = 'Left'
    if lr:
        b50 = 'Right'
    fs1, b35 = wavfile.read((file_wav.split('\\'))[-1] + '_L_aux.wav')
    b36 = b35.T[lr]
    b37 = [(ele / 2**8.) * 2 - 1 for ele in b36]
    b38 = fft(b37)
    b39 = len(b38) / 2
    fs2, b40 = wavfile.read((file_wav.split('\\'))[-1] + '_M_aux.wav')
    b41 = b40.T[lr]
    b42 = [(ele / 2**8.) * 2 - 1 for ele in b41]
    b43 = fft(b42)
    b44 = len(b43) / 2
    fs3, b45 = wavfile.read((file_wav.split('\\'))[-1] + '_H_aux.wav')
    b46 = b45.T[lr]
    b47 = [(ele / 2**8.) * 2 - 1 for ele in b46]
    b48 = fft(b47)
    b49 = len(b48) / 2
    b29 = tk.Tk()
    b29.wm_title(b50 + (file_wav.split('\\'))[-1] + 'Low_Mid_Hi' + b50)
    b30 = plt.figure(figsize=(5, 4), dpi=100)
    b30.add_subplot(611).plot(abs(b38[:int(b39 - 1)]), 'r')
    b30.add_subplot(612).plot(b37[:int(b39 - 1)], 'r')
    b30.add_subplot(613).plot(abs(b43[:int(b44 - 1)]), 'r')
    b30.add_subplot(614).plot(b42[:int(b44 - 1)], 'r')
    b30.add_subplot(615).plot(abs(b48[:int(b49 - 1)]), 'r')
    b30.add_subplot(616).plot(b47[:int(b49 - 1)], 'r')
    b31 = FigureCanvasTkAgg(b30, master=b29)
    b31.draw()
    b31.get_tk_widget().pack(b32 = tk.TOP, fill=tk.BOTH, expand=1)
    b33 = NavigationToolbar2Tk(b31, b29)
    b33.update()
    b31.get_tk_widget().pack(b32 = tk.TOP, fill=tk.BOTH, expand=1)
    def fonk16(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, b31, b33)
    b31.mpl_connect("key_press_event", on_key_press)
    def fonk17():
        b29.quit()
        b29.destroy()
    b34 = tk.Button(master=b29, text="Quit", command=_quit)
    b34.pack(b32 = tk.BOTTOM)
    tk.mainloop()
def fonk18():
    global b51
    b51 = filedialog.askopenfilename()
def fonk19():
    global b52
    b52 = filedialog.askopenfilename()
def fonk20():
    global b51
    fonk9(b51)
def fonk21():
    global b52
    fonk9(b52)
def fonk22():
    global b51
    global b52
    b53 = (b51.split('\\'))[-1] + (b52.split('\\'))[-1]
    try:
        wavfile.read(b53)
    except:
        fonk5(b51, b52, b53)
    fonk9(b53)
def fonk23(filename):
    fonk6(filename, True, 0, 255, 0)
    fonk6(filename, True, 2, 256, 2000)
    fonk6(filename, True, 1, 2001, 0)
    fonk12(filename)
def fonk24(filename):
    print('LR')
    fonk7(filename, 0, 255, 0)
    fonk7(filename, 2, 256, 2000)
    fonk7(filename, 1, 2001, 0)
    print('L')
    fonk15(filename, 0)
def fonk25(filename):
    print('LR')
    fonk7(filename, 0, 255, 0)
    fonk7(filename, 2, 256, 2000)
    fonk7(filename, 1, 2001, 0)
    print('R')
    fonk15(filename, 1)
def fonk26():
    global b51
    rate, b12 = wavfile.read(b51)
    try:
        b13 = len(b12[0])
        rate, b12 = None, None
        print('hi there')
        fonk24(b51)
    except Exception as e:
        rate, b12 = None, None
        print('hi there_x', e, b12)
        fonk23(b51)
def fonk27():
    global b52
    rate, b12 = wavfile.read(b52)
    try:
        b13 = len(b12[0])
        rate, b12 = None, None
        fonk24(b52)
    except:
        rate, b12 = None, None
        fonk23(b52)
def fonk28():
    global b51
    rate, b12 = wavfile.read(b51)
    try:
        b13 = len(b12[0])
        rate, b12 = None, None
        print('hi there')
        fonk25(b51)
    except Exception as e:
        rate, b12 = None, None
        print('hi there_x', e, b12)
        fonk23(b51)
def fonk29():
    global b52
    rate, b12 = wavfile.read(b52)
    try:
        b13 = len(b12[0])
        rate, b12 = None, None
        fonk25(b52)
    except:
        rate, b12 = None, None
        fonk23(b52)
def fonk30():
    global b51
    global b52
    b53 = (b51.split('\\'))[-1] + (b52.split('\\'))[-1]
    fonk23(b53)
def fonk31():
    import os
    os._exit(0)