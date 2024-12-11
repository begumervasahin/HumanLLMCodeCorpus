from scipy.io import wavfile
import wave, struct, math
import numpy as np
b38 = 44100
b39 = b38 / 2.0
b43 = 512
def fonk1(b25, b44 = 0, b6=0):
        b25 /= (b39 / (b43 / 2.0))
        b44 /= (b39 / (b43 / 2.0))
        b49 = []
        b4 = []
        b5 = b43
        for f in range(0, b5+1):
                b48 = 1.0
                if not b6:
                    if f > b25:
                            b48 = 0
                    b49.append(b48)
                    if f > 0 and f < b5:
                            b4.append(b48)
                elif b6 = = 1:
                    if f < b25:
                            b48 = 0
                    b49.append(b48)
                    if f > 0 and f < b5:
                            b4.append(b48)
                else:
                    if f < b25 or f > b44:
                            b48 = 0
                    b49.append(b48)
                    if f > 0 and f < b5:
                            b4.append(b48)
        b4.reverse()
        b49 = b49 + b4
        b7 = np.fft.ifft(b49).real.tolist()
        b8 = b7[:b43
        b9 = b7[b43
        b7 = b9 + b8
        b10 = b43
        for n in range(0, b10):
                    b7[n] *= (n + 0.0) / b10
        for n in range(b10 + 1, b43):
                    b7[n] *= (b43 - n + 0.0) / b10
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
def fonk6(inpt, b15, b22 = 0,b40=4500, b45=0):
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
            b14 = np.convolve(b14, fonk1(b25=b40, b44=b45, b6=b22))
        wavfile.write(inpt+b23,rate,b14.astype(np.int16))
        print('Step - ok')
    except:
        if b15 = = True:
            b12 = np.convolve(b12, fonk1(b25=b40, b44=b45, b6=b22))
        wavfile.write(inpt+b23,rate,b12.astype(np.int16))
        print('Step - ok but exception')
def fonk7(inpt, b22 = 0,b40=4500, b45=0):
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
        b24[...,i] = np.convolve(b12[...,i], fonk1(b25 = b40, b44=b45, b6=b22))[:len(b24[...,i])]
    wavfile.write(inpt+b23,rate,b24.astype(np.int16))
    print('Step - ok')
def fonk8(file_wav):
  import matplotlib.pyplot as plt
  from scipy.fftpack import fft
  from scipy.io import wavfile
  fs, b26 = wavfile.read(file_wav)
  b27 = b26.T
  b10 = [(ele/2**8.)*2-1 for ele in b27]
  b28 = fft(b10)
  b29 = len(b28)/2
  plt.plot(abs(b28[:int(b29-1)]),'r')
  plt.show()
  plt.plot(b10[:int(b29-1)],'r')
  plt.show()
from easygui import *
import sys
def fonk9(file_wav):
    import tkinter
    from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    import numpy as np
    from matplotlib.figure import Figure
    from scipy.fftpack import fft
    from scipy.io import wavfile
    fs, b26 = wavfile.read(file_wav)
    try:
        from operator import add
        b27 = list(map(add, b26.T[0], b26.T[1]))
    except:
        print('EX')
        b27 = b26.T[0]
    b10 = [(ele/2**8.)*2-1 for ele in b27]
    b28 = fft(b10)
    b29 = len(b28)/2
    b30 = tkinter.Tk()
    b30.wm_title((file_wav.split('\\'))[-1])
    b31 = Figure(figsize=(5, 4), dpi=100)
    b32 = np.arange(0, 3, .01)
    b31.add_subplot(211).plot(abs(b28[:int(b29-1)]),'r')
    b31.add_subplot(212).plot(b10[:int(b29-1)],'r')
    b33 = FigureCanvasTkAgg(b31, master=b30)
    b33.draw()
    b33.get_tk_widget().pack(b34 = tkinter.TOP, fill=tkinter.BOTH, expand=1)
    b35 = NavigationToolbar2Tk(b33, b30)
    b35.update()
    b33.get_tk_widget().pack(b34 = tkinter.TOP, fill=tkinter.BOTH, expand=1)
    def fonk10(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, b33, b35)
    b33.mpl_connect("key_press_event", on_key_press)
    def fonk11():
        b30.quit()
        b30.destroy()
    b36 = tkinter.Button(master=b30, b59="Quit", command=_quit)
    b36.pack(b34 = tkinter.BOTTOM)
    tkinter.mainloop()
def fonk12(file_wav):
    import tkinter
    from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    import numpy as np
    from matplotlib.figure import Figure
    from scipy.fftpack import fft
    from scipy.io import wavfile
    fs1, b37 = wavfile.read((file_wav.split('\\'))[-1]+ '_L_aux.wav')
    b38 = b37.T
    b39 = [(ele/2**8.)*2-1 for ele in b38]
    b40 = fft(b39)
    b41 = len(b40)/2
    fs2, b42 = wavfile.read((file_wav.split('\\'))[-1]+ '_M_aux.wav')
    b43 = b42.T
    b44 = [(ele/2**8.)*2-1 for ele in b43]
    b45 = fft(b44)
    b46 = len(b45)/2
    fs3, b47 = wavfile.read((file_wav.split('\\'))[-1]+ '_H_aux.wav')
    b48 = b47.T
    b49 = [(ele/2**8.)*2-1 for ele in b48]
    b50 = fft(b49)
    b51 = len(b50)/2
    b30 = tkinter.Tk()
    b30.wm_title((file_wav.split('\\'))[-1] + 'Low_Mid_Hi')
    b31 = Figure(figsize=(5, 4), dpi=100)
    b32 = np.arange(0, 3, .01)
    b31.add_subplot(611).plot(abs(b40[:int(b41-1)]),'r')
    b31.add_subplot(612).plot(b39[:int(b41-1)],'r')
    b31.add_subplot(613).plot(abs(b45[:int(b46-1)]),'r')
    b31.add_subplot(614).plot(b44[:int(b46-1)],'r')
    b31.add_subplot(615).plot(abs(b50[:int(b51-1)]),'r')
    b31.add_subplot(616).plot(b49[:int(b51-1)],'r')
    b33 = FigureCanvasTkAgg(b31, master=b30)
    b33.draw()
    b33.get_tk_widget().pack(b34 = tkinter.TOP, fill=tkinter.BOTH, expand=1)
    b35 = NavigationToolbar2Tk(b33, b30)
    b35.update()
    b33.get_tk_widget().pack(b34 = tkinter.TOP, fill=tkinter.BOTH, expand=1)
    def fonk13(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, b33, b35)
    b33.mpl_connect("key_press_event", on_key_press)
    def fonk14():
        b30.quit()
        b30.destroy()
    b36 = tkinter.Button(master=b30, b59="Quit", command=_quit)
    b36.pack(b34 = tkinter.BOTTOM)
    tkinter.mainloop()
def fonk15(file_wav,lr):
    b52 = 'Left'
    if lr:
        b52 = 'Right'
    import tkinter
    from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    import numpy as np
    from matplotlib.figure import Figure
    from scipy.fftpack import fft
    from scipy.io import wavfile
    fs1, b37 = wavfile.read((file_wav.split('\\'))[-1]+ '_L_aux.wav')
    b38 = b37.T[lr]
    b39 = [(ele/2**8.)*2-1 for ele in b38]
    b40 = fft(b39)
    b41 = len(b40)/2
    fs2, b42 = wavfile.read((file_wav.split('\\'))[-1]+ '_M_aux.wav')
    b43 = b42.T[lr]
    b44 = [(ele/2**8.)*2-1 for ele in b43]
    b45 = fft(b44)
    b46 = len(b45)/2
    fs3, b47 = wavfile.read((file_wav.split('\\'))[-1]+ '_H_aux.wav')
    b48 = b47.T[lr]
    b49 = [(ele/2**8.)*2-1 for ele in b48]
    b50 = fft(b49)
    b51 = len(b50)/2
    b30 = tkinter.Tk()
    b30.wm_title(b52+ (file_wav.split('\\'))[-1] + 'Low_Mid_Hi'+b52)
    b31 = Figure(figsize=(5, 4), dpi=100)
    b32 = np.arange(0, 3, .01)
    b31.add_subplot(611).plot(abs(b40[:int(b41-1)]),'r')
    b31.add_subplot(612).plot(b39[:int(b41-1)],'r')
    b31.add_subplot(613).plot(abs(b45[:int(b46-1)]),'r')
    b31.add_subplot(614).plot(b44[:int(b46-1)],'r')
    b31.add_subplot(615).plot(abs(b50[:int(b51-1)]),'r')
    b31.add_subplot(616).plot(b49[:int(b51-1)],'r')
    b33 = FigureCanvasTkAgg(b31, master=b30)
    b33.draw()
    b33.get_tk_widget().pack(b34 = tkinter.TOP, fill=tkinter.BOTH, expand=1)
    b35 = NavigationToolbar2Tk(b33, b30)
    b35.update()
    b33.get_tk_widget().pack(b34 = tkinter.TOP, fill=tkinter.BOTH, expand=1)
    def fonk16(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, b33, b35)
    b33.mpl_connect("key_press_event", on_key_press)
    def fonk17():
        b30.quit()
        b30.destroy()
    b36 = tkinter.Button(master=b30, b59="Quit", command=_quit)
    b36.pack(b34 = tkinter.BOTTOM)
    tkinter.mainloop()
b53 = ''
b54 = ''
def fonk18():
    global b53
    b53 = fileopenbox()
def fonk19():
    global b54
    b54 = fileopenbox()
def fonk20():
    global b53
    fonk9(b53)
def fonk21():
    global b54
    fonk9(b54)
def fonk22():
    global b53
    global b54
    b55 = (b53.split('\\'))[-1]+(b54.split('\\'))[-1]
    try:
        wavfile.read(b55)
    except:
        fonk5(b53, b54, b55)
    fonk9(b55)
def fonk23(filename):
    fonk6(filename, True,0, 255,0)
    fonk6(filename, True,2, 256,2000)
    fonk6(filename, True,1, 2001,0)
    fonk12(filename)
def fonk24(filename):
    print('LR')
    fonk7(filename,0, 255,0)
    fonk7(filename,2, 256,2000)
    fonk7(filename,1, 2001,0)
    print('L')
    fonk15(filename, 0)
def fonk25(filename):
    print('LR')
    fonk7(filename,0, 255,0)
    fonk7(filename,2, 256,2000)
    fonk7(filename,1, 2001,0)
    print('R')
    fonk15(filename, 1)
def fonk26():
    global b53
    rate, b12 = wavfile.read(b53)
    try:
        b13 = len(b12[0])
        rate, b12 = None, None
        print('hi there')
        fonk24(b53)
    except Exception as e:
        rate, b12 = None, None
        print('hi there_x', e, b12)
        fonk23(b53)
def fonk27():
    global b54
    rate, b12 = wavfile.read(b54)
    try:
        b13 = len(b12[0])
        rate, b12 = None, None
        fonk24(b54)
    except:
        rate, b12 = None, None
        fonk23(b54)
def fonk28():
    global b53
    rate, b12 = wavfile.read(b53)
    try:
        b13 = len(b12[0])
        rate, b12 = None, None
        print('hi there')
        fonk25(b53)
    except Exception as e:
        rate, b12 = None, None
        print('hi there_x', e, b12)
        fonk23(b53)
def fonk29():
    global b54
    rate, b12 = wavfile.read(b54)
    try:
        b13 = len(b12[0])
        rate, b12 = None, None
        fonk25(b54)
    except:
        rate, b12 = None, None
        fonk23(b54)
def fonk30():
    global b53
    global b54
    b55 = (b53.split('\\'))[-1]+(b54.split('\\'))[-1]
    fonk23(b55)
def fonk31():
    import os
    os._exit(0)
import tkinter as tk
b30 = tk.Tk()
b56 = "MCT_MDO"
b30.title(b56)
b30.columnconfigure(0, b57 = 1)
b30.rowconfigure(0, b57 = 1)
b58 = ["import song1","import song2","plot song1","plot song2","plot_song_stegano"]
tk.Label(b30, b59 = "Martinescu_Danoiu_Orbisor_343A3").grid(b61=0, column=0, columnspan = len(b58), stick="n", pady=(15,0))
b60 = tk.Frame(b30)
b60.grid(b61 = 2, column=0)
tk.Button(b60, b59 = b58[0],command = get_name_1).grid(b61=0, column=0, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = b58[1], command = get_name_2).grid(b61=0, column=1, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = 'low mid high L song1', command = get_l_m_h1l).grid(b61=0, column=2, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = 'low mid high R song1', command = get_l_m_h1r).grid(b61=0, column=3, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = b58[2], command = get_plot_1).grid(b61=0, column=4, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = b58[3], command = get_plot_2).grid(b61=0, column=5, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = 'low mid high L song2', command = get_l_m_h2l).grid(b61=0, column=6, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = 'low mid high R song2', command = get_l_m_h2r).grid(b61=0, column=7, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = b58[4], command = get_plot_12).grid(b61=0, column=8, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = 'low mid high both songs', command = get_l_m_h12).grid(b61=0, column=9, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(b60, b59 = 'EXIT', command = exit_m8).grid(b61=0, column=10, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
b30.mainloop()