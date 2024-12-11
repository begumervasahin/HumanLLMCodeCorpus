import tensorflow as tf
a1 = 2048
a2 = 2048
def fonk1(pcm, b1 = 24, sample_rate=44100.0):
    b2 = tf.signal.stft(pcm, frame_length=a2, frame_step=a1, fft_length=a2)
    b3 = tf.abs(b2, name="b3")
    b4 = b3.shape[-1]
    lower_edge_hertz, upper_edge_hertz, b5 = 80.0, 7600.0, 64
    b6 = tf.signal.b6(
            b5, b4, sample_rate, lower_edge_hertz,
            upper_edge_hertz)
    b7 = tf.tensordot(b3, b6, 1)
    b7.set_shape(b3.shape[:-1].concatenate(
        b6.shape[-1:]))
    a3 = 1e-6
    b8 = tf.math.log(b7 + a3)
    b9 = tf.signal.mfccs_from_log_mel_spectrograms(
            b8)[..., :b1]
    return b9
b10 = tf.placeholder(tf.float32, [None], name="source_pcm")
b11 = tf.placeholder(tf.float32, [None], name="b11")
b12 = fonk1(b10)
b13 = fonk1(b11)
b14 = tf.matmul(b12, tf.transpose(b13))
b15 = tf.norm(b12, axis=1)
b16 = tf.norm(b13, axis=1)
b17 = tf.matmul(tf.reshape(b15, (-1, 1)), tf.reshape(b16, (1, -1)))
b18 = tf.divide(b14, b17)
b19 = tf.acos(b18, name="angular_distance")
b20 = tf.argmin(b19, axis=0)
b21 = tf.multiply(b20, a1, name="b21")
b22 = tf.compat.v1.get_default_graph().as_graph_def()
b23 = './'
tf.io.write_graph(b22, b23, 'model.pb', b24 = False)