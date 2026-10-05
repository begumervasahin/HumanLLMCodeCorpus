import tkinter as tk
from easygui import fileopenbox
from scipy.io import wavfile
import numpy as np
import wave
import struct
import math
from scipy.fftpack import fft
import matplotlib.pyplot as plt
b34 = 44100
b35 = b34 / 2.0
b39 = 512
def fonk1(b25, b40 = 0, b6=0):
    b25 /= (b35 / (b39 / 2.0))
    b40 /= (b35 / (b39 / 2.0))
    b45 = []
    b4 = []
    b5 = b39
    for f in range(0, b5+1):
        b44 = 1.0
        if not b6:
            if f > b25:
                b44 = 0
            b45.append(b44)
            if f > 0 and f < b5:
                b4.append(b44)
        elif b6 = = 1:
            if f < b25:
                b44 = 0
            b45.append(b44)
            if f > 0 and f < b5:
                b4.append(b44)
        else:
            if f < b25 or f > b40:
                b44 = 0
            b45.append(b44)
            if f > 0 and f < b5:
                b4.append(b44)
    b4.reverse()
    b45 = b45 + b4
    b7 = np.fft.ifft(b45).real.tolist()
    b8 = b7[:b39
    b9 = b7[b39
    b7 = b9 + b8
    b10 = b39
    for n in range(0, b10):
        b7[n] *= (n + 0.0) / b10
    for n in range(b10 + 1, b39):
        b7[n] *= (b39 - n + 0.0) / b10
    return b7
def fonk2(original, cutoff):
    b11 = fonk1(b25=cutoff, b6=0)
    return np.convolve(original, b11)
def fonk3(inpt, b15):
    rate, b12 = wavfile.read(inpt)
    try:
        b13 = len(b12[0])
        b14 = (np.array([0]*len(b12[...,0]))).astype(np.float)
        for i in range(b13):
            b14 += 1/b13*(b12[...,i]).astype(np.float)
        if b15 = = True:
            b14 = 2*fonk2(1/2*b14,4500)
        wavfile.write(inpt+'aux.wav',rate,b14.astype(np.int16))
        print('Step - ok')
    except:
        if b15 = = True:
            b12 = 2*fonk2(1/2*b12,4500)
        wavfile.write(inpt+'aux.wav',rate,b12.astype(np.int16))
        print('Step - ok but exception')
def fonk4(inpt1, inpt2, output):
    b16 = wave.open(inpt1+'aux.wav', "r")
    b17 = wave.open(inpt2+'aux.wav', "r")
    b18 = wave.open(output, "w")
    for f in [b18]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    a4 = 0
    for n in range(0, b16.getnframes()):
        b19 = (struct.unpack('h', b16.readframes(1))[0] / 32768.0)/2
        if a4 < b17.getnframes():
            b20 = struct.unpack('h', b17.readframes(1))[0] / 32768.0
            b21 = math.cos(22050.0 * (a4 / 44100.0) * math.pi * 2)
            b19 += b20 * b21 / 4
            a4 += 1
        b18.writeframes(struct.pack('h', int(b19 * 32767)))
def fonk5(inpt1, inpt2, output):
    fonk3(inpt2, True)
    fonk3(inpt1, False)
    fonk4(inpt1, inpt2, output)
def fonk6(inpt, b15, b22 = 0,b36=4500, b41=0):
    rate, b12 = wavfile.read(inpt)
    b23 = 'aux.wav'
    if b22 = = 0:
        b23 = '_L_'+b23
    elif b22 = = 2:
        b23 = '_M_'+b23
    else:
        b23 = '_H_'+b23
    try:
        b13 = len(b12[0])
        b14 = (np.array([0]*len(b12[...,0]))).astype(np.float)
        for i in range(b13):
            b14 += 1/b13*(b12[...,i]).astype(np.float)
        if b15 = = True:
            b14 = np.convolve(b14, fonk1(b25=b36, b40=b41, b6=b22))
        wavfile.write(inpt+b23,rate,b14.astype(np.int16))
        print('Step - ok')
    except:
        if b15 = = True:
            b12 = np.convolve(b12, fonk1(b25=b36, b40=b41, b6=b22))
        wavfile.write(inpt+b23,rate,b12.astype(np.int16))
        print('Step - ok but exception')
def fonk7(inpt, b22 = 0,b36=4500, b41=0):
    rate, b12 = wavfile.read(inpt)
    b23 = 'aux.wav'
    if b22 = = 0:
        b23 = '_L_'+b23
    elif b22 = = 2:
        b23 = '_M_'+b23
    else:
        b23 = '_H_'+b23
    b24 = ((np.array([0]*2*len(b12[...,0]))).astype(np.float)).reshape(len(b12[...,0]), len(b12[0]))
    print(len(b12[...,0]), len(b12[0]))
    print(b24)
    print(len(b12))
    for i in range(len(b12[0])):
        b24[...,i] = np.convolve(b12[...,i], fonk1(b25 = b36, b40=b41, b6=b22))[:len(b24[...,i])]
    wavfile.write(inpt+b23,rate,b24.astype(np.int16))
    print('Step - ok')
def fonk8(file_wav):
    fs, b26 = wavfile.read(file_wav)
    b27 = b26.T
    b10 = [(ele/2**8.)*2-1 for ele in b27]
    b28 = fft(b10)
    b29 = len(b28)/2
    plt.plot(abs(b28[:int(b29-1)]),'r')
    plt.show()
    plt.plot(b10[:int(b29-1)],'r')
    plt.show()
def fonk9(file_wav):
    fs, b26 = wavfile.read(file_wav)
    try:
        b27 = list(map(lambda x: x[0]+x[1], zip(b26.T[0], b26.T[1])))
    except:
        b27 = b26.T[0]
    b10 = [(ele/2**8.)*2-1 for ele in b27]
    b28 = fft(b10)
    b29 = len(b28)/2
    b30 = tk.Tk()
    b30.wm_title((file_wav.split('\\'))[-1])
    b31 = plt.figure(figsize=(5, 4), dpi=100)
    b32 = np.arange(0, 3, .01)
    b31.add_subplot(211).plot(abs(b28[:int(b29-1)]),'r')
    b31.add_subplot(212).plot(b10[:int(b29-1)],'r')
    plt.show()
def fonk10(file_wav):
    fs1, b33 = wavfile.read((file_wav.split('\\'))[-1]+ '_L_aux.wav')
    b34 = b33.T
    b35 = [(ele/2**8.)*2-1 for ele in b34]
    b36 = fft(b35)
    b37 = len(b36)/2
    fs2, b38 = wavfile.read((file_wav.split('\\'))[-1]+ '_M_aux.wav')
    b39 = b38.T
    b40 = [(ele/2**8.)*2-1 for ele in b39]
    b41 = fft(b40)
    b42 = len(b41)/2
    fs3, b43 = wavfile.read((file_wav.split('\\'))[-1]+ '_H_aux.wav')
    b44 = b43.T
    b45 = [(ele/2**8.)*2-1 for ele in b44]
    b46 = fft(b45)
    b47 = len(b46)/2
    b30 = tk.Tk()
    b30.wm_title((file_wav.split('\\'))[-1] + 'Low_Mid_Hi')
    b31 = plt.figure(figsize=(5, 4), dpi=100)
    b32 = np.arange(0, 3, .01)
    b31.add_subplot(611).plot(abs(b36[:int(b37-1)]),'r')
    b31.add_subplot(612).plot(b35[:int(b37-1)],'r')
    b31.add_subplot(613).plot(abs(b41[:int(b42-1)]),'r')
    b31.add_subplot(614).plot(b40[:int(b42-1)],'r')
    b31.add_subplot(615).plot(abs(b46[:int(b47-1)]),'r')
    b31.add_subplot(616).plot(b45[:int(b47-1)],'r')
    plt.show()
def fonk11(file_wav,lr):
    b48 = 'Left'
    if lr:
        b48 = 'Right'
    fs1, b33 = wavfile.read((file_wav.split('\\'))[-1]+ '_L_aux.wav')
    b34 = b33.T[lr]
    b35 = [(ele/2**8.)*2-1 for ele in b34]
    b36 = fft(b35)
    b37 = len(b36)/2
    fs2, b38 = wavfile.read((file_wav.split('\\'))[-1]+ '_M_aux.wav')
    b39 = b38.T[lr]
    b40 = [(ele/2**8.)*2-1 for ele in b39]
    b41 = fft(b40)
    b42 = len(b41)/2
    fs3, b43 = wavfile.read((file_wav.split('\\'))[-1]+ '_H_aux.wav')
    b44 = b43.T[lr]
    b45 = [(ele/2**8.)*2-1 for ele in b44]
    b46 = fft(b45)
    b47 = len(b46)/2
    b30 = tk.Tk()
    b30.wm_title(b48+ (file_wav.split('\\'))[-1] + 'Low_Mid_Hi'+b48)
    b31 = plt.figure(figsize=(5, 4), dpi=100)
    b32 = np.arange(0, 3, .01)
    b31.add_subplot(611).plot(abs(b36[:int(b37-1)]),'r')
    b31.add_subplot(612).plot(b35[:int(b37-1)],'r')
    b31.add_subplot(613).plot(abs(b41[:int(b42-1)]),'r')
    b31.add_subplot(614).plot(b40[:int(b42-1)],'r')
    b31.add_subplot(615).plot(abs(b46[:int(b47-1)]),'r')
    b31.add_subplot(616).plot(b45[:int(b47-1)],'r')
    plt.show()
def fonk12():
    global b49
    b49 = fileopenbox()
def fonk13():
    global b50
    b50 = fileopenbox()
def fonk14():
    global b49
    fonk9(b49)
def fonk15():
    global b50
    fonk9(b50)
b30 = tk.Tk()
b51 = "MCT_MDO"
b30.title(b51)
b30.columnconfigure(0, b52 = 1)
b30.rowconfigure(0, b52 = 1)
b53 = ["import song1","import song2","plot song1","plot song2","plot_song_stegano"]
tk.Label(b30, b54 = "Martinescu_Danoiu_Orbisor_343A3").grid(b56=0, column=0, columnspan=len(b53), stick="n", pady=(15,0))
b55 = tk.Frame(b30)
b55.grid(b56 = 2, column=0)
tk.Button(b55, b54 = b53[0], command=get_name_1).grid(b56=0, column=0, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = b53[1], command=get_name_2).grid(b56=0, column=1, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = 'low mid high L song1', command=get_l_m_h1l).grid(b56=0, column=2, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = 'low mid high R song1', command=get_l_m_h1r).grid(b56=0, column=3, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = b53[2], command=get_plot_1).grid(b56=0, column=4, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = b53[3], command=get_plot_2).grid(b56=0, column=5, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = 'low mid high L song2', command=get_l_m_h2l).grid(b56=0, column=6, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = 'low mid high R song2', command=get_l_m_h2r).grid(b56=0, column=7, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = b53[4], command=get_plot_12).grid(b56=0, column=8, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = 'low mid high both songs', command=get_l_m_h12).grid(b56=0, column=9, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b55, b54 = 'EXIT', command=exit_m8).grid(b56=0, column=10, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
b30.mainloop()