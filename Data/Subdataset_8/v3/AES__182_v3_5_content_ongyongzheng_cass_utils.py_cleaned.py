import numpy as np
import librosa
def reverse_stft(magnitude, phase):
    nsample = magnitude * np.exp(1j * phase)
    nsample = np.array(librosa.core.istft(nsample, hop_length=768))
    return nsample
def compute_lx_error(x, y, phase, norm=2):
    errors = []
    for i in range(x.shape[0]):
        phase_sample = phase[i]
        x_sample = reverse_stft(x[i], phase_sample)
        y_sample = reverse_stft(y[i], phase_sample)
        error = np.linalg.norm(y_sample - x_sample, ord=norm)
        errors.append(error)
    return np.nanmean(errors)
def compute_sdr(x, y, phase, mag):
    sdr_values = []
    for i in range(x.shape[0]):
        phase_sample = phase[i]
        x_sample = reverse_stft(x[i], phase_sample)
        y_sample = reverse_stft(y[i], phase_sample)
        noise_power = np.sqrt(np.mean(np.square(x_sample - y_sample))) + 1e-16
        target_power = np.sqrt(np.mean(np.square(y_sample)))
        if target_power / noise_power != 0:
            sdr = 20 * np.log10(target_power / noise_power)
            sdr_values.append(sdr)
    return (np.nanmean(sdr_values), np.nanstd(sdr_values),
            np.nanmedian(sdr_values), np.nanmin(sdr_values),
            np.nanmax(sdr_values))