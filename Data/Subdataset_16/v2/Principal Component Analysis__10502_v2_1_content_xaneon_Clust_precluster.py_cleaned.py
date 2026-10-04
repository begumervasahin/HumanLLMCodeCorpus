import numpy as np
import princomp
import thresh
import spktimes
import get_stimtrigavs
import spkwaveform
import filter_spikes
def fonk1(signal, sampling_rate, spike_window_duration):
    b1 = signal.copy()
    b2 = filter_spikes.high_pass(signal, sampling_rate, 1000, 3)
    b2 = filter_spikes.low_pass(b2, sampling_rate, sampling_rate / 2.0, 1)
    b3 = thresh.detect(b2, 'manual')
    b4 = spktimes.detect(b2, b3)
    b5 = np.where(b4 == True)[0]
    b6 = b5 / float(sampling_rate)
    b7 = get_stimtrigavs.get_avs(b2, sampling_rate, b6, spike_window_duration, 'zeros')
    b6, b7 = spkwaveform.align(b6, b7, spike_window_duration, sampling_rate)
    b6, b7 = spkwaveform.window_detect(b6, b7, [0.0005, 0.001], sampling_rate * 10, 'manual')
    b8 = {}
    b8['coeff'], b8['score'], b8['latent'] = princomp.get(b7)
    b7 = get_stimtrigavs.get_avs(b1, sampling_rate, b6, spike_window_duration, 'zeros')
    b9 = b7.max(axis=1)
    b6, b7 = spkwaveform.align(b6, b7, spike_window_duration, sampling_rate)
    return b3, b6, b9, b7, b8