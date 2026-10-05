import numpy as np
import wave
import struct
SAMPLE_WIDTH_STRUCT = {
    1: 'b',
    2: 'h'
}
def open_wave_file(filename):
    with wave.open(filename, 'r') as file:
        nchannels = file.getnchannels()
        sampwidth = file.getsampwidth()
        framerate = file.getframerate()
        nframes = file.getnframes()
        struct_format = f"<{nframes}{SAMPLE_WIDTH_STRUCT[sampwidth]}"
        frames = file.readframes(nframes)
        samples = np.array(struct.unpack(struct_format, frames))
        return nchannels, sampwidth, framerate, nframes, samples
def save_wave_file(filename, headers, samples):
    nchannels, sampwidth, framerate, nframes = headers
    samples = np.clip(samples[:nframes], -2**(sampwidth*8-1), 2**(sampwidth*8-1)-1)
    struct_format = f"<{nframes}{SAMPLE_WIDTH_STRUCT[sampwidth]}"
    with wave.open(filename, 'w') as file:
        file.setnchannels(nchannels)
        file.setsampwidth(sampwidth)
        file.setframerate(framerate)
        file.setnframes(nframes)
        frames = struct.pack(struct_format, *samples)
        file.writeframes(frames)
