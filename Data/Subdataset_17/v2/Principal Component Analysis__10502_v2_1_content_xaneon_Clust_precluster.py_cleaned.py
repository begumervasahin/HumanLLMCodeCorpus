import numpy as np
import princomp
import thresh
import spktimes
import get_stimtrigavs
import spkwaveform
import filter_spikes
def precluster_signal(signal, sampling_rate, spike_window_duration):
    original_signal = signal.copy()
    filtered_signal = filter_spikes.high_pass(signal, sampling_rate, 1000, 3)
    filtered_signal = filter_spikes.low_pass(filtered_signal, sampling_rate, sampling_rate / 2.0, 1)
    threshold = thresh.detect(filtered_signal, 'manual')
    spikes_detected = spktimes.detect(filtered_signal, threshold)
    spike_indices = np.where(spikes_detected == True)[0]
    spike_times = spike_indices / float(sampling_rate)
    spike_waveforms = get_stimtrigavs.get_avs(filtered_signal, sampling_rate, spike_times, spike_window_duration, 'zeros')
    spike_times, spike_waveforms = spkwaveform.align(spike_times, spike_waveforms, spike_window_duration, sampling_rate)
    spike_times, spike_waveforms = spkwaveform.window_detect(spike_times, spike_waveforms, [0.0005, 0.001], sampling_rate * 10, 'manual')
    principal_components = {}
    principal_components['coeff'], principal_components['score'], principal_components['latent'] = princomp.get(spike_waveforms)
    spike_waveforms = get_stimtrigavs.get_avs(original_signal, sampling_rate, spike_times, spike_window_duration, 'zeros')
    spike_heights = spike_waveforms.max(axis=1)
    spike_times, spike_waveforms = spkwaveform.align(spike_times, spike_waveforms, spike_window_duration, sampling_rate)
    return threshold, spike_times, spike_heights, spike_waveforms, principal_components