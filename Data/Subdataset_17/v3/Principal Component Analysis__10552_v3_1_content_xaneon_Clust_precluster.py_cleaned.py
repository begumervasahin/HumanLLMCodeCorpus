import numpy as np
import princomp
import thresh
import spktimes
import get_stimtrigavs
import spkwaveform
import filter_spikes
def precluster_signal(signal, sampling_rate, spike_window_duration):
    original_signal = signal.copy()
    filtered_signal = apply_filters(signal, sampling_rate)
    threshold = detect_threshold(filtered_signal)
    spike_times = detect_spikes(filtered_signal, threshold, sampling_rate)
    spike_waveforms = extract_spike_waveforms(filtered_signal, spike_times, spike_window_duration, sampling_rate)
    spike_times, spike_waveforms = align_waveforms(spike_times, spike_waveforms, spike_window_duration, sampling_rate)
    spike_times, spike_waveforms = perform_window_detection(spike_times, spike_waveforms, sampling_rate)
    principal_components = calculate_principal_components(spike_waveforms)
    spike_heights, spike_waveforms = recalculate_and_align_waveforms(original_signal, spike_times, spike_window_duration, sampling_rate)
    return threshold, spike_times, spike_heights, spike_waveforms, principal_components
def apply_filters(signal, sampling_rate):
    filtered_signal = filter_spikes.high_pass(signal, sampling_rate, 1000, 3)
    filtered_signal = filter_spikes.low_pass(filtered_signal, sampling_rate, sampling_rate / 2.0, 1)
    return filtered_signal
def detect_threshold(filtered_signal):
    return thresh.detect(filtered_signal, 'manual')
def detect_spikes(filtered_signal, threshold, sampling_rate):
    spikes_detected = spktimes.detect(filtered_signal, threshold)
    spike_indices = np.where(spikes_detected == True)[0]
    return spike_indices / float(sampling_rate)
def extract_spike_waveforms(filtered_signal, spike_times, spike_window_duration, sampling_rate):
    return get_stimtrigavs.get_avs(filtered_signal, sampling_rate, spike_times, spike_window_duration, 'zeros')
def align_waveforms(spike_times, spike_waveforms, spike_window_duration, sampling_rate):
    return spkwaveform.align(spike_times, spike_waveforms, spike_window_duration, sampling_rate)
def perform_window_detection(spike_times, spike_waveforms, sampling_rate):
    return spkwaveform.window_detect(spike_times, spike_waveforms, [0.0005, 0.001], sampling_rate * 10, 'manual')
def calculate_principal_components(spike_waveforms):
    principal_components = {}
    principal_components['coeff'], principal_components['score'], principal_components['latent'] = princomp.get(spike_waveforms)
    return principal_components
def recalculate_and_align_waveforms(original_signal, spike_times, spike_window_duration, sampling_rate):
    spike_waveforms = get_stimtrigavs.get_avs(original_signal, sampling_rate, spike_times, spike_window_duration, 'zeros')
    spike_heights = spike_waveforms.max(axis=1)
    spike_times, spike_waveforms = spkwaveform.align(spike_times, spike_waveforms, spike_window_duration, sampling_rate)
    return spike_heights, spike_waveforms