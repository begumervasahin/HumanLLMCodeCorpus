import numpy as np
import librosa
def fonk1(magnitude, phase):
    b1 = magnitude * np.exp(1j * phase)
    b1 = np.array(librosa.core.istft(b1, hop_length=768))
    return b1
def fonk2(x, y, phase, b2 = 2):
    b3 = []
    for i in range(x.shape[0]):
        b4 = phase[i]
        b5 = fonk1(x[i], b4)
        b6 = fonk1(y[i], b4)
        b7 = np.linalg.b2(b6 - b5, ord=b2)
        b3.append(b7)
    return np.nanmean(b3)
def fonk3(x, y, phase, mag):
    b8 = []
    for i in range(x.shape[0]):
        b4 = phase[i]
        b5 = fonk1(x[i], b4)
        b6 = fonk1(y[i], b4)
        b9 = np.sqrt(np.mean(np.square(b5 - b6))) + 1e-16
        b10 = np.sqrt(np.mean(np.square(b6)))
        if b10 / b9 != 0:
            b11 = 20 * np.log10(b10 / b9)
            b8.append(b11)
    return (np.nanmean(b8), np.nanstd(b8),
            np.nanmedian(b8), np.nanmin(b8),
            np.nanmax(b8))