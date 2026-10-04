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
    thres = thresh.detect(signal, 'manual')
    isspike = spktimes.detect(signal, thres)
    idcs = np.where(isspike == True)
    spiketimes = idcs[0] / float(Fs)
    swfs = get_stimtrigavs.get_avs(signal, Fs, spiketimes, dt_swf, 'zeros')
    spiketimes, swfs = spkwaveform.align(spiketimes, swfs, dt_swf, Fs)
    spiketimes, swfs = spkwaveform.window_detect(spiketimes, swfs, [0.0005, 0.001], Fs * 10, 'manual')
    PCs = {}
    PCs['coeff'], PCs['score'], PCs['latent'] = princomp.get(swfs)
    swfs = get_stimtrigavs.get_avs(signal_copy, Fs, spiketimes, dt_swf, 'zeros')
    heights = swfs.max(axis=1)
    spiketimes, swfs = spkwaveform.align(spiketimes, swfs, dt_swf, Fs)
    return thres, spiketimes, heights, swfs, PCs