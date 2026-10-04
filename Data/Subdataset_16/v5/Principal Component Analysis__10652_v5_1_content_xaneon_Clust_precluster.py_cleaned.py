
import numpy as np
import princomp
import thresh
import spktimes
import get_stimtrigavs
import spkwaveform
import filter_spikes
def fonk1(b2, Fs, dt_swf):
    b1 = b2.copy()
    b2 = filter_spikes.high_pass(b2, Fs, 1000, 3)
    b2 = filter_spikes.low_pass(b2, Fs, Fs / 2.0, 1)
    b3 = thresh.detect(b2, 'manual')
    b4 = spktimes.detect(b2, b3)
    b5 = np.where(b4)[0]
    b6 = b5 / float(Fs)
    b7 = get_stimtrigavs.get_avs(b2, Fs, b6, dt_swf, 'zeros')
    b6, b7 = spkwaveform.align(b6, b7, dt_swf, Fs)
    b6, b7 = spkwaveform.window_detect(b6, b7, [0.0005, 0.001], Fs * 10, 'manual')
    b8 = fonk2(b7)
    b7 = get_stimtrigavs.get_avs(b1, Fs, b6, dt_swf, 'zeros')
    b9 = b7.max(axis=1)
    b6, b7 = spkwaveform.align(b6, b7, dt_swf, Fs)
    return b3, b6, b9, b7, b8
def fonk2(b7):
    coeff, score, b10 = princomp.fonk1(b7)
    b8 = {
        'coeff': coeff,
        'score': score,
        'b10': b10
    }
    return b8