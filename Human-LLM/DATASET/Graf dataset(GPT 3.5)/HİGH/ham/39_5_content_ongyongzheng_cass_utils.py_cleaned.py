import numpy as np
import librosa
def fonk1(imag, phase):
    b1 = imag
    b2 = b1 * np.exp(1j*phase)
    b2 = np.array(librosa.core.istft(b2, hop_length=768))
    return b2
def fonk2(x, y, phase, b3 = 2):
    b4 = []
    for i in range(x.shape[0]):
        b5 = phase[i]
        b6 = fonk1(x[i],b5)
        b7 = fonk1(y[i],b5)
        b4.append(
            np.linalg.norm(b7-b6, b8 = b3))
    return np.nanmean(np.array(b4))
def fonk3(x, y, phase, mag):
    b4 = []
    for i in range(x.shape[0]):
        b5 = phase[i]
        b6 = fonk1(x[i],b5)
        b7 = fonk1(y[i],b5)
        b9 = np.sqrt(np.mean(np.square(b6-b7)))+1e-16
        b10 = np.sqrt(np.mean(np.square(b7)))
        if b10/b9 != 0:
            b4.append(20*np.log10(b10/b9))
    return np.nanmean(b4), np.nanstd(b4), np.nanmedian(b4), np.nanmin(b4), np.nanmax(b4)