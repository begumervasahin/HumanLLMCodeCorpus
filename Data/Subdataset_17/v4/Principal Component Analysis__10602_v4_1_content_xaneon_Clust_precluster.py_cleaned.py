
import numpy as np
import princomp
import thresh
import spktimes
import get_stimtrigavs
import spkwaveform
import filter_spikes
def get(signal, Fs, dt_swf):
    signal_copy = signal.copy()
    signal = filter_spikes.high_pass(signal, Fs, 1000, 3)
    signal = filter_spikes.low_pass(signal, Fs, Fs / 2.0, 1)
    threshold = thresh.detect(signal, 'manual')
    is_spike = spktimes.detect(signal, threshold)
    spike_indices = np.where(is_spike)[0]
    spike_times = spike_indices / float(Fs)
    spike_waveforms = get_stimtrigavs.get_avs(signal, Fs, spike_times, dt_swf, 'zeros')
    spike_times, spike_waveforms = spkwaveform.align(spike_times, spike_waveforms, dt_swf, Fs)
    spike_times, spike_waveforms = spkwaveform.window_detect(spike_times, spike_waveforms, [0.0005, 0.001], Fs * 10, 'manual')
    PCs = dict()
    PCs['coeff'], PCs['score'], PCs['latent'] = princomp.get(spike_waveforms)
    spike_waveforms = get_stimtrigavs.get_avs(signal_copy, Fs, spike_times, dt_swf, 'zeros')
    spike_heights = spike_waveforms.max(axis=1)
    spike_times, spike_waveforms = spkwaveform.align(spike_times, spike_waveforms, dt_swf, Fs)
    return threshold, spike_times, spike_heights, spike_waveforms, PCs