import tkinter as tk
from easygui import fileopenbox
from scipy.io import wavfile
import numpy as np
import wave
import struct
import math
from scipy.fftpack import fft
import matplotlib.pyplot as plt
SAMPLE_RATE = 44100
NYQUIST_RATE = SAMPLE_RATE / 2.0
FFT_LENGTH = 512
def create_lowpass_filter(cutoff1, cutoff2=0, filter_type=0):
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
def apply_lowpass_filter(original, cutoff):
    coefs = create_lowpass_filter(cutoff1=cutoff, filter_type=0)
    return np.convolve(original, coefs)
def convert_stereo_to_mono(input_file, apply_filter):
    rate, audio = wavfile.read(input_file)
    try:
        nr_of_channels = len(audio[0])
        mono_frame = np.mean(audio, axis=1)
        if apply_filter:
            mono_frame = 2 * apply_lowpass_filter(0.5 * mono_frame, 4500)
        wavfile.write(input_file + 'aux.wav', rate, mono_frame.astype(np.int16))
        print('Step - ok')
    except:
        if apply_filter:
            audio = 2 * apply_lowpass_filter(0.5 * audio, 4500)
        wavfile.write(input_file + 'aux.wav', rate, audio.astype(np.int16))
        print('Step - ok but exception')
def am_modulate(input_file1, input_file2, output_file):
    baseband1 = wave.open(input_file1 + 'aux.wav', "r")
    baseband2 = wave.open(input_file2 + 'aux.wav', "r")
    amsc = wave.open(output_file, "w")
    for f in [amsc]:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
    contor = 0
    for n in range(0, baseband1.getnframes()):
        base = (struct.unpack('h', baseband1.readframes(1))[0] / 32768.0) / 2
        if contor < baseband2.getnframes():
            encod_frame = struct.unpack('h', baseband2.readframes(1))[0] / 32768.0
            carrier_sample = math.cos(22050.0 * (contor / 44100.0) * math.pi * 2)
            base += encod_frame * carrier_sample / 4
            contor += 1
        amsc.writeframes(struct.pack('h', int(base * 32767)))
def modulate_am(input_file1, input_file2, output_file):
    convert_stereo_to_mono(input_file2, True)
    convert_stereo_to_mono(input_file1, False)
    am_modulate(input_file1, input_file2, output_file)
def apply_filter_low_mid_high(input_file, apply_filter, l_m_h=0, c1=4500, c2=0):
    rate, audio = wavfile.read(input_file)
    var = 'aux.wav'
    if l_m_h == 0:
        var = '_L_' + var
    elif l_m_h == 2:
        var = '_M_' + var
    else:
        var = '_H_' + var
    try:
        nr_of_channels = len(audio[0])
        mono_frame = np.mean(audio, axis=1)
        if apply_filter:
            mono_frame = np.convolve(mono_frame, create_lowpass_filter(cutoff1=c1, cutoff2=c2, filter_type=l_m_h))
        wavfile.write(input_file + var, rate, mono_frame.astype(np.int16))
        print('Step - ok')
    except:
        if apply_filter:
            audio = np.convolve(audio, create_lowpass_filter(cutoff1=c1, cutoff2=c2, filter_type=l_m_h))
        wavfile.write(input_file + var, rate, audio.astype(np.int16))
        print('Step - ok but exception')
def filter_low_mid_high(input_file, l_m_h=0, c1=4500, c2=0):
    rate, audio = wavfile.read(input_file)
    var = 'aux.wav'
    if l_m_h == 0:
        var = '_L_' + var
    elif l_m_h == 2:
        var = '_M_' + var
    else:
        var = '_H_' + var
    audio_aux = np.zeros((2 * len(audio[...,0]), len(audio[0])))
    for i in range(len(audio[0])):
        audio_aux[...,i] = np.convolve(audio[...,i], create_lowpass_filter(cutoff1=c1, cutoff2=c2, filter_type=l_m_h))[:len(audio_aux[...,i])]
    wavfile.write(input_file + var, rate, audio_aux.astype(np.int16))
    print('Step - ok')
def plot_waveform_and_spectrum(file_wav):
    fs, data = wavfile.read(file_wav)
    a = data.T
    b = [(ele / 2 ** 8.) * 2 - 1 for ele in a]
    c = fft(b)
    d = len(c) / 2
    plt.plot(abs(c[:int(d - 1)]), 'r')
    plt.show()
    plt.plot(b[:int(d - 1)], 'r')
    plt.show()
def plot_waveform_and_spectrum_stereo(file_wav):
    fs, data = wavfile.read(file_wav)
    try:
        a = list(map(lambda x: x[0] + x[1], zip(data.T[0], data.T[1])))
    except:
        a = data.T[0]
    b = [(ele / 2 ** 8.) * 2 - 1 for ele in a]
    c = fft(b)
    d = len(c) / 2
    root = tk.Tk()
    root.wm_title((file_wav.split('\\'))[-1])
    fig = plt.figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(211).plot(abs(c[:int(d - 1)]), 'r')
    fig.add_subplot(212).plot(b[:int(d - 1)], 'r')
    plt.show()
def plot_low_mid_high_spectrum(file_wav):
    fs1, data1 = wavfile.read((file_wav.split('\\'))[-1] + '_L_aux.wav')
    a1 = data1.T
    b1 = [(ele / 2 ** 8.) * 2 - 1 for ele in a1]
    c1 = fft(b1)
    d1 = len(c1) / 2
    fs2, data2 = wavfile.read((file_wav.split('\\'))[-1] + '_M_aux.wav')
    a2 = data2.T
    b2 = [(ele / 2 ** 8.) * 2 - 1 for ele in a2]
    c2 = fft(b2)
    d2 = len(c2) / 2
    fs3, data3 = wavfile.read((file_wav.split('\\'))[-1] + '_H_aux.wav')
    a3 = data3.T
    b3 = [(ele / 2 ** 8.) * 2 - 1 for ele in a3]
    c3 = fft(b3)
    d3 = len(c3) / 2
    root = tk.Tk()
    root.wm_title((file_wav.split('\\'))[-1] + 'Low_Mid_Hi')
    fig = plt.figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(611).plot(abs(c1[:int(d1 - 1)]), 'r')
    fig.add_subplot(612).plot(b1[:int(d1 - 1)], 'r')
    fig.add_subplot(613).plot(abs(c2[:int(d2 - 1)]), 'r')
    fig.add_subplot(614).plot(b2[:int(d2 - 1)], 'r')
    fig.add_subplot(615).plot(abs(c3[:int(d3 - 1)]), 'r')
    fig.add_subplot(616).plot(b3[:int(d3 - 1)], 'r')
    plt.show()
def plot_low_mid_high_spectrum_lr(file_wav, lr):
    tt = 'Left'
    if lr:
        tt = 'Right'
    fs1, data1 = wavfile.read((file_wav.split('\\'))[-1] + '_L_aux.wav')
    a1 = data1.T[lr]
    b1 = [(ele / 2 ** 8.) * 2 - 1 for ele in a1]
    c1 = fft(b1)
    d1 = len(c1) / 2
    fs2, data2 = wavfile.read((file_wav.split('\\'))[-1] + '_M_aux.wav')
    a2 = data2.T[lr]
    b2 = [(ele / 2 ** 8.) * 2 - 1 for ele in a2]
    c2 = fft(b2)
    d2 = len(c2) / 2
    fs3, data3 = wavfile.read((file_wav.split('\\'))[-1] + '_H_aux.wav')
    a3 = data3.T[lr]
    b3 = [(ele / 2 ** 8.) * 2 - 1 for ele in a3]
    c3 = fft(b3)
    d3 = len(c3) / 2
    root = tk.Tk()
    root.wm_title(tt + (file_wav.split('\\'))[-1] + 'Low_Mid_Hi' + tt)
    fig = plt.figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(611).plot(abs(c1[:int(d1 - 1)]), 'r')
    fig.add_subplot(612).plot(b1[:int(d1 - 1)], 'r')
    fig.add_subplot(613).plot(abs(c2[:int(d2 - 1)]), 'r')
    fig.add_subplot(614).plot(b2[:int(d2 - 1)], 'r')
    fig.add_subplot(615).plot(abs(c3[:int(d3 - 1)]), 'r')
    fig.add_subplot(616).plot(b3[:int(d3 - 1)], 'r')
    plt.show()
def select_song1():
    global filename1
    filename1 = fileopenbox()
def select_song2():
    global filename2
    filename2 = fileopenbox()
def plot_song1():
    global filename1
    plot_waveform_and_spectrum_stereo(filename1)
def plot_song2():
    global filename2
    plot_waveform_and_spectrum_stereo(filename2)
def plot_both_songs():
    global filename1, filename2
    plot_waveform_and_spectrum_stereo(filename1)
    plot_waveform_and_spectrum_stereo(filename2)
root = tk.Tk()
version = "MCT_MDO"
root.title(version)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_options = [
    "Import Song 1",
    "Import Song 2",
    "Plot Song 1",
    "Plot Song 2",
    "Plot Both Songs"
]
tk.Label(root, text="Martinescu_Danoiu_Orbisor_343A3").grid(row=0, column=0, columnspan=len(main_options), stick="n", pady=(15,0))
frame2 = tk.Frame(root)
frame2.grid(row=2, column=0)
tk.Button(frame2, text=main_options[0], command=select_song1).grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(frame2, text=main_options[1], command=select_song2).grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(frame2, text=main_options[2], command=plot_song1).grid(row=0, column=2, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(frame2, text=main_options[3], command=plot_song2).grid(row=0, column=3, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(frame2, text=main_options[4], command=plot_both_songs).grid(row=0, column=4, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
tk.Button(frame2, text='Exit', command=root.destroy).grid(row=0, column=5, ipadx=5, ipady=5, padx=5, pady=(30, 5), stick="ew")
root.mainloop()