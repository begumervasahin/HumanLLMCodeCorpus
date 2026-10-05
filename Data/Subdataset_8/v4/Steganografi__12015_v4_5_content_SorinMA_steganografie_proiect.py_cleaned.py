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
SAMPLE_RATE = 44100
NYQUIST_RATE = SAMPLE_RATE / 2.0
FFT_LENGTH = 512
def filter_pass(cutoff1, cutoff2=0, filter_type=0):
    cutoff1 /= (NYQUIST_RATE / (FFT_LENGTH / 2.0))
    cutoff2 /= (NYQUIST_RATE / (FFT_LENGTH / 2.0))
    mask = []
    negatives = []
    l = FFT_LENGTH
    for f in range(0, l+1):
        rampdown = 1.0
        if not filter_type:
            if f > cutoff1:
                rampdown = 0
        elif filter_type == 1:
            if f < cutoff1:
                rampdown = 0
        else:
            if f < cutoff1 or f > cutoff2:
                rampdown = 0
        mask.append(rampdown)
        if f > 0 and f < l:
            negatives.append(rampdown)
    negatives.reverse()
    mask = mask + negatives
    impulse_response = np.fft.ifft(mask).real.tolist()
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
    coefs = filter_pass(cutoff1=cutoff, filter_type=0)
    return np.convolve(original, coefs)
def fromNto1Ch(inpt, filter_audio):
    rate, audio = wavfile.read(inpt)
    try:
        nrOfChannels = len(audio[0])
        monoChFrame = np.sum(audio, axis=1) / nrOfChannels
        if filter_audio:
            monoChFrame = 2 * lowpass(0.5 * monoChFrame, 4500)
        wavfile.write(inpt + 'aux.wav', rate, monoChFrame.astype(np.int16))
        print('Step - ok')
    except:
        if filter_audio:
            audio = 2 * lowpass(0.5 * audio, 4500)
        wavfile.write(inpt + 'aux.wav', rate, audio.astype(np.int16))
        print('Step - ok but exception')
def am_modulation(inpt1, inpt2, output):
    baseband1 = wave.open(inpt1 + 'aux.wav', "r")
    baseband2 = wave.open(inpt2 + 'aux.wav', "r")
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
def mod_am(inpt1, inpt2, output):
    fromNto1Ch(inpt2, True)
    fromNto1Ch(inpt1, False)
    am_modulation(inpt1, inpt2, output)
def fromNto1Ch_low_midi_high(inpt, filter_audio, l_m_h=0, c1=4500, c2=0):
    rate, audio = wavfile.read(inpt)
    var = 'aux.wav'
    if l_m_h == 0:
        var = '_L_' + var
    elif l_m_h == 2:
        var = '_M_' + var
    else:
        var = '_H_' + var
    try:
        nrOfChannels = len(audio[0])
        monoChFrame = np.sum(audio, axis=1) / nrOfChannels
        if filter_audio:
            monoChFrame = np.convolve(monoChFrame, filter_pass(cutoff1=c1, cutoff2=c2, filter_type=l_m_h))
        wavfile.write(inpt + var, rate, monoChFrame.astype(np.int16))
        print('Step - ok')
    except:
        if filter_audio:
            audio = np.convolve(audio, filter_pass(cutoff1=c1, cutoff2=c2, filter_type=l_m_h))
        wavfile.write(inpt + var, rate, audio.astype(np.int16))
        print('Step - ok but exception')
def low_midi_high(inpt, l_m_h=0, c1=4500, c2=0):
    rate, audio = wavfile.read(inpt)
    var = 'aux.wav'
    if l_m_h == 0:
        var = '_L_' + var
    elif l_m_h == 2:
        var = '_M_' + var
    else:
        var = '_H_' + var
    audio_aux = np.zeros((len(audio[...,0]) * 2, len(audio[0])))
    for i in range(len(audio[0])):
        audio_aux[...,i] = np.convolve(audio[...,i], filter_pass(cutoff1=c1, cutoff2=c2, filter_type=l_m_h))[:len(audio_aux[...,i])]
    wavfile.write(inpt + var, rate, audio_aux.astype(np.int16))
    print('Step - ok')
def get_plot(file_wav):
    fs, data = wavfile.read(file_wav)
    a = data.T
    b = [(ele / 2**8.) * 2 - 1 for ele in a]
    c = fft(b)
    d = len(c) / 2
    plt.plot(abs(c[:int(d - 1)]), 'r')
    plt.show()
    plt.plot(b[:int(d - 1)], 'r')
    plt.show()
def get_plot_v2(file_wav):
    fs, data = wavfile.read(file_wav)
    try:
        a = np.sum(data.T, axis=0)
    except:
        a = data.T[0]
    b = [(ele / 2**8.) * 2 - 1 for ele in a]
    c = fft(b)
    d = len(c) / 2
    root = tk.Tk()
    root.wm_title((file_wav.split('\\'))[-1])
    fig = plt.figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(211).plot(abs(c[:int(d - 1)]), 'r')
    fig.add_subplot(212).plot(b[:int(d - 1)], 'r')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    def _quit():
        root.quit()
        root.destroy()
    button = tk.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tk.BOTTOM)
    tk.mainloop()
def get_plot_v2_l_m_h(file_wav):
    fs1, data1 = wavfile.read((file_wav.split('\\'))[-1] + '_L_aux.wav')
    a1 = data1.T
    b1 = [(ele / 2**8.) * 2 - 1 for ele in a1]
    c1 = fft(b1)
    d1 = len(c1) / 2
    fs2, data2 = wavfile.read((file_wav.split('\\'))[-1] + '_M_aux.wav')
    a2 = data2.T
    b2 = [(ele / 2**8.) * 2 - 1 for ele in a2]
    c2 = fft(b2)
    d2 = len(c2) / 2
    fs3, data3 = wavfile.read((file_wav.split('\\'))[-1] + '_H_aux.wav')
    a3 = data3.T
    b3 = [(ele / 2**8.) * 2 - 1 for ele in a3]
    c3 = fft(b3)
    d3 = len(c3) / 2
    root = tk.Tk()
    root.wm_title((file_wav.split('\\'))[-1] + 'Low_Mid_Hi')
    fig = plt.figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(611).plot(abs(c1[:int(d1 - 1)]), 'r')
    fig.add_subplot(612).plot(b1[:int(d1 - 1)], 'r')
    fig.add_subplot(613).plot(abs(c2[:int(d2 - 1)]), 'r')
    fig.add_subplot(614).plot(b2[:int(d2 - 1)], 'r')
    fig.add_subplot(615).plot(abs(c3[:int(d3 - 1)]), 'r')
    fig.add_subplot(616).plot(b3[:int(d3 - 1)], 'r')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    def _quit():
        root.quit()
        root.destroy()
    button = tk.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tk.BOTTOM)
    tk.mainloop()
def get_plot_v2_l_m_h_lr(file_wav, lr):
    tt = 'Left'
    if lr:
        tt = 'Right'
    fs1, data1 = wavfile.read((file_wav.split('\\'))[-1] + '_L_aux.wav')
    a1 = data1.T[lr]
    b1 = [(ele / 2**8.) * 2 - 1 for ele in a1]
    c1 = fft(b1)
    d1 = len(c1) / 2
    fs2, data2 = wavfile.read((file_wav.split('\\'))[-1] + '_M_aux.wav')
    a2 = data2.T[lr]
    b2 = [(ele / 2**8.) * 2 - 1 for ele in a2]
    c2 = fft(b2)
    d2 = len(c2) / 2
    fs3, data3 = wavfile.read((file_wav.split('\\'))[-1] + '_H_aux.wav')
    a3 = data3.T[lr]
    b3 = [(ele / 2**8.) * 2 - 1 for ele in a3]
    c3 = fft(b3)
    d3 = len(c3) / 2
    root = tk.Tk()
    root.wm_title(tt + (file_wav.split('\\'))[-1] + 'Low_Mid_Hi' + tt)
    fig = plt.figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(611).plot(abs(c1[:int(d1 - 1)]), 'r')
    fig.add_subplot(612).plot(b1[:int(d1 - 1)], 'r')
    fig.add_subplot(613).plot(abs(c2[:int(d2 - 1)]), 'r')
    fig.add_subplot(614).plot(b2[:int(d2 - 1)], 'r')
    fig.add_subplot(615).plot(abs(c3[:int(d3 - 1)]), 'r')
    fig.add_subplot(616).plot(b3[:int(d3 - 1)], 'r')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    def _quit():
        root.quit()
        root.destroy()
    button = tk.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tk.BOTTOM)
    tk.mainloop()
def get_name_1():
    global filename1
    filename1 = filedialog.askopenfilename()
def get_name_2():
    global filename2
    filename2 = filedialog.askopenfilename()
def get_plot_1():
    global filename1
    get_plot_v2(filename1)
def get_plot_2():
    global filename2
    get_plot_v2(filename2)
def get_plot_12():
    global filename1
    global filename2
    aux_file = (filename1.split('\\'))[-1] + (filename2.split('\\'))[-1]
    try:
        wavfile.read(aux_file)
    except:
        mod_am(filename1, filename2, aux_file)
    get_plot_v2(aux_file)
def get_l_m_h(filename):
    fromNto1Ch_low_midi_high(filename, True, 0, 255, 0)
    fromNto1Ch_low_midi_high(filename, True, 2, 256, 2000)
    fromNto1Ch_low_midi_high(filename, True, 1, 2001, 0)
    get_plot_v2_l_m_h(filename)
def get_l_m_h_l(filename):
    print('LR')
    low_midi_high(filename, 0, 255, 0)
    low_midi_high(filename, 2, 256, 2000)
    low_midi_high(filename, 1, 2001, 0)
    print('L')
    get_plot_v2_l_m_h_lr(filename, 0)
def get_l_m_h_r(filename):
    print('LR')
    low_midi_high(filename, 0, 255, 0)
    low_midi_high(filename, 2, 256, 2000)
    low_midi_high(filename, 1, 2001, 0)
    print('R')
    get_plot_v2_l_m_h_lr(filename, 1)
def get_l_m_h1l():
    global filename1
    rate, audio = wavfile.read(filename1)
    try:
        nrOfChannels = len(audio[0])
        rate, audio = None, None
        print('hi there')
        get_l_m_h_l(filename1)
    except Exception as e:
        rate, audio = None, None
        print('hi there_x', e, audio)
        get_l_m_h(filename1)
def get_l_m_h2l():
    global filename2
    rate, audio = wavfile.read(filename2)
    try:
        nrOfChannels = len(audio[0])
        rate, audio = None, None
        get_l_m_h_l(filename2)
    except:
        rate, audio = None, None
        get_l_m_h(filename2)
def get_l_m_h1r():
    global filename1
    rate, audio = wavfile.read(filename1)
    try:
        nrOfChannels = len(audio[0])
        rate, audio = None, None
        print('hi there')
        get_l_m_h_r(filename1)
    except Exception as e:
        rate, audio = None, None
        print('hi there_x', e, audio)
        get_l_m_h(filename1)
def get_l_m_h2r():
    global filename2
    rate, audio = wavfile.read(filename2)
    try:
        nrOfChannels = len(audio[0])
        rate, audio = None, None
        get_l_m_h_r(filename2)
    except:
        rate, audio = None, None
        get_l_m_h(filename2)
def get_l_m_h12():
    global filename1
    global filename2
    aux_file = (filename1.split('\\'))[-1] + (filename2.split('\\'))[-1]
    get_l_m_h(aux_file)
def exit_m8():
    import os
    os._exit(0)