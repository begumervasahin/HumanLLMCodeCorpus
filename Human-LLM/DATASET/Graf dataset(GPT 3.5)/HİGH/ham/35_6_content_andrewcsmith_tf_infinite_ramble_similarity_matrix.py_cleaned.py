import tensorflow as tf
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import librosa
from librosa import display
from tensorflow.python import debug as tf_debug
a1 = 2048
a2 = 2048
b1 = tf.ConfigProto()
b1.gpu_options.b2 = True
b3 = tf.Session(b1=b1)
b4 = [tf_debug.LocalCLIDebugHook()]
def fonk1(pcm, b5 = 24, sample_rate=44100.0):
    b6 = tf.contrib.signal.stft(pcm, frame_length=a2, frame_step=a1, fft_length=a2)
    b7 = tf.abs(b6, name="b7")
    b8 = b7.shape[-1].value
    lower_edge_hertz, upper_edge_hertz, b9 = 80.0, 7600.0, 64
    b10 = tf.contrib.signal.b10(
            b9, b8, sample_rate, lower_edge_hertz,
            upper_edge_hertz)
    b11 = tf.tensordot(b7, b10, 1)
    b11.set_shape(b7.shape[:-1].concatenate(
        b10.shape[-1:]))
    a3 = 1e-6
    b12 = tf.log(b11 + a3)
    b13 = tf.contrib.signal.mfccs_from_log_mel_spectrograms(
            b12)[..., :b5]
    return b13
b14 = tf.placeholder(tf.float32, [None], name="source_pcm")
b15 = tf.placeholder(tf.float32, [None], name="b15")
b16 = fonk1(b14)
b17 = fonk1(b15)
b18 = tf.matmul(b16, tf.transpose(b17))
b19 = tf.norm(b16, axis=1)
b20 = tf.norm(b17, axis=1)
b21 = tf.matmul(tf.reshape(b19, (-1, 1)), tf.reshape(b20, (1, -1)))
b22 = tf.divide(b18, b21)
b23 = tf.acos(b22, name="angular_distance")
b24 = tf.argmin(b23, axis=0)
b25 = tf.multiply(b24, a1, name="b25")
b26 = b3.graph_def
b27 = './'
tf.train.write_graph(b26, b27, 'model.pb', b28 = False)