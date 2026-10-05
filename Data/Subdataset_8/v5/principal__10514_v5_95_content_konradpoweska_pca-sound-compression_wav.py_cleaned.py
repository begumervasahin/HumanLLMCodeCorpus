import numpy as np
import wave
import struct
SAMPLE_WIDTH_FORMAT = {
    1: 'b',
    2: 'h'
}
def open_wav(filename):
    with wave.open(filename, 'r') as wav_file:
        nchannels = wav_file.getnchannels()
        sampwidth = wav_file.getsampwidth()
        framerate = wav_file.getframerate()
        nframes = wav_file.getnframes()
        headers = (nchannels, sampwidth, framerate, nframes)
        struct_format = f"<{nframes}{SAMPLE_WIDTH_FORMAT[sampwidth]}"
        frames = wav_file.readframes(nframes)
        samples = np.array(struct.unpack(struct_format, frames))
    return headers, samples
def save_wav(filename, headers, samples):
    nchannels, sampwidth, framerate, nframes = headers
    samples = np.clip(samples[:nframes], -2**(sampwidth*8-1), 2**(sampwidth*8-1)-1)
    struct_format = f"<{nframes}{SAMPLE_WIDTH_FORMAT[sampwidth]}"
    frames = struct.pack(struct_format, *samples)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(nchannels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.setnframes(nframes)
        wav_file.writeframes(frames)