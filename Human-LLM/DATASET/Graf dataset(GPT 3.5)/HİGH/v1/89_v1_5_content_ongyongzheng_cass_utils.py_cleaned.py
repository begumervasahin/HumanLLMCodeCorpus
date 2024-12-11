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
        b3.append(np.linalg.norm(b6 - b5, b7 = b2))
    return np.nanmean(np.array(b3))
def fonk3(x, y, phase, mag):
    b3 = []
    for i in range(x.shape[0]):
        b4 = phase[i]
        b5 = fonk1(x[i], b4)
        b6 = fonk1(y[i], b4)
        b8 = np.sqrt(np.mean(np.square(b5 - b6))) + 1e-16
        b9 = np.sqrt(np.mean(np.square(b6)))
        if b9 / b8 != 0:
            b3.append(20 * np.log10(b9 / b8))
    return np.nanmean(b3), np.nanstd(b3), np.nanmedian(b3), np.nanmin(b3), np.nanmax(b3)
