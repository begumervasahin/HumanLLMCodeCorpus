import numpy as np
import princomp
import thresh
import spktimes
import get_stimtrigavs
import spkwaveform
import filter_spikes
def fonk1(signal, sampling_rate, spike_window_duration):
    b1 = signal.copy()
    b2 = fonk2(signal, sampling_rate)
    b3 = fonk3(b2)
    b4 = fonk4(b2, b3, sampling_rate)
    b5 = fonk5(b2, b4, spike_window_duration, sampling_rate)
    b4, b5 = fonk6(b4, b5, spike_window_duration, sampling_rate)
    b4, b5 = fonk7(b4, b5, sampling_rate)
    b6 = fonk8(b5)
    b9, b5 = fonk9(b1, b4, spike_window_duration, sampling_rate)
    return b3, b4, b9, b5, b6
def fonk2(signal, sampling_rate):
    b2 = filter_spikes.high_pass(signal, sampling_rate, 1000, 3)
    b2 = filter_spikes.low_pass(b2, sampling_rate, sampling_rate / 2.0, 1)
    return b2
def fonk3(b2):
    return thresh.detect(b2, 'manual')
def fonk4(b2, b3, sampling_rate):
    b7 = spktimes.detect(b2, b3)
    b8 = np.where(b7 == True)[0]
    return b8 / float(sampling_rate)
def fonk5(b2, b4, spike_window_duration, sampling_rate):
    return get_stimtrigavs.get_avs(b2, sampling_rate, b4, spike_window_duration, 'zeros')
def fonk6(b4, b5, spike_window_duration, sampling_rate):
    return spkwaveform.align(b4, b5, spike_window_duration, sampling_rate)
def fonk7(b4, b5, sampling_rate):
    return spkwaveform.window_detect(b4, b5, [0.0005, 0.001], sampling_rate * 10, 'manual')
def fonk8(b5):
    b6 = {}
    b6['coeff'], b6['score'], b6['latent'] = princomp.get(b5)
    return b6
def fonk9(b1, b4, spike_window_duration, sampling_rate):
    b5 = get_stimtrigavs.get_avs(b1, sampling_rate, b4, spike_window_duration, 'zeros')
    b9 = b5.max(axis=1)
    b4, b5 = spkwaveform.align(b4, b5, spike_window_duration, sampling_rate)
    return b9, b5