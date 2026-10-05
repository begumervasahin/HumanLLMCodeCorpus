import tensorflow as tf
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import librosa
from librosa import display
from tensorflow.python import debug as tf_debug
HOP = 2048
BIN = 2048
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
hooks = [tf_debug.LocalCLIDebugHook()]
def generate_mfcc_graph(pcm, num_mfccs=24, sample_rate=44100.0):
    stfts = tf.contrib.signal.stft(pcm, frame_length=BIN, frame_step=HOP, fft_length=BIN)
    spectrograms = tf.abs(stfts, name="spectrograms")
    num_spectrogram_bins = spectrograms.shape[-1].value
    lower_edge_hertz, upper_edge_hertz, num_mel_bins = 80.0, 7600.0, 64
    linear_to_mel_weight_matrix = tf.contrib.signal.linear_to_mel_weight_matrix(
            num_mel_bins, num_spectrogram_bins, sample_rate, lower_edge_hertz,
            upper_edge_hertz)
    mel_spectrograms = tf.tensordot(spectrograms, linear_to_mel_weight_matrix, 1)
    mel_spectrograms.set_shape(spectrograms.shape[:-1].concatenate(
        linear_to_mel_weight_matrix.shape[-1:]))
    log_offset = 1e-6
    log_mel_spectrograms = tf.log(mel_spectrograms + log_offset)
    mfccs = tf.contrib.signal.mfccs_from_log_mel_spectrograms(
            log_mel_spectrograms)[..., :num_mfccs]
    return mfccs
full_source_pcm = tf.placeholder(tf.float32, [None], name="source_pcm")
target_pcm = tf.placeholder(tf.float32, [None], name="target_pcm")
full_source_mfccs = generate_mfcc_graph(full_source_pcm)
target_mfccs = generate_mfcc_graph(target_pcm)
dot = tf.matmul(full_source_mfccs, tf.transpose(target_mfccs))
full_source_norms = tf.norm(full_source_mfccs, axis=1)
target_norms = tf.norm(target_mfccs, axis=1)
norm_dot = tf.matmul(tf.reshape(full_source_norms, (-1, 1)), tf.reshape(target_norms, (1, -1)))
similarity_matrix = tf.divide(dot, norm_dot)
angular = tf.acos(similarity_matrix, name="angular_distance")
best_match = tf.argmin(angular, axis=0)
start_frames = tf.multiply(best_match, HOP, name="start_frames")
definition = sess.graph_def
directory = './'
tf.train.write_graph(definition, directory, 'model.pb', as_text=False)