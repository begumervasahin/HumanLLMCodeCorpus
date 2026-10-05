import tensorflow as tf
a1 = 2048
a2 = 2048
b1 = tf.ConfigProto()
b1.gpu_options.b2 = True
b3 = tf.Session(b1=b1)
def fonk1(pcm, b4 = 24, sample_rate=44100.0):
    b5 = tf.contrib.signal.stft(pcm, frame_length=a2, frame_step=a1, fft_length=a2)
    b6 = tf.abs(b5, name="b6")
    b7 = b6.shape[-1].value
    lower_edge_hertz, upper_edge_hertz, b8 = 80.0, 7600.0, 64
    b9 = tf.contrib.signal.b9(
        b8, b7, sample_rate, lower_edge_hertz, upper_edge_hertz)
    b10 = tf.tensordot(b6, b9, 1)
    b10.set_shape(b6.shape[:-1].concatenate(b9.shape[-1:]))
    a3 = 1e-6
    b11 = tf.log(b10 + a3)
    b12 = tf.contrib.signal.mfccs_from_log_mel_spectrograms(b11)[..., :b4]
    return b12
b13 = tf.placeholder(tf.float32, [None], name="source_pcm")
b14 = tf.placeholder(tf.float32, [None], name="b14")
b15 = fonk1(b13)
b16 = fonk1(b14)
b17 = tf.matmul(b15, tf.transpose(b16))
b18 = tf.norm(b15, axis=1)
b19 = tf.norm(b16, axis=1)
b20 = tf.matmul(tf.reshape(b18, (-1, 1)), tf.reshape(b19, (1, -1)))
b21 = tf.divide(b17, b20)
b22 = tf.acos(b21, name="b22")
b23 = tf.argmin(b22, axis=0)
b24 = tf.multiply(b23, a1, name="b24")
b25 = b3.b25
b26 = './'
tf.train.write_graph(b25, b26, 'model.pb', b27 = False)