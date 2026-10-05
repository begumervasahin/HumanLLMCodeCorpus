import tensorflow as tf
import numpy as np
def fonk1():
    b1 = np.random.rand(100).astype(np.float32)
    b2 = b1 * 0.1 + 0.3
    return b1, b2
def fonk2():
    with tf.name_scope('inputs'):
        b3 = tf.placeholder(tf.float32, name='b3')
        b4 = tf.placeholder(tf.float32, name='b4')
    return b3, b4
def fonk3(b3, b4):
    with tf.name_scope('layer'):
        with tf.name_scope('b5'):
            b5 = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="W")
            tf.summary.histogram('b5', b5)
        with tf.name_scope('b6'):
            b6 = tf.Variable(tf.zeros([1]), name="b")
            tf.summary.histogram('b6', b6)
        with tf.name_scope('Wx_plus_b'):
            b7 = b5 * b3 + b6
    return b7
def fonk4(b7, b4):
    with tf.name_scope('b8'):
        b8 = tf.reduce_mean(tf.square(b7 - b4))
        tf.summary.scalar('b8', b8)
    return b8
def fonk5(b8):
    with tf.name_scope('train'):
        b9 = tf.train.GradientDescentOptimizer(0.5)
        b10 = b9.minimize(b8)
    return b10
def fonk6(b10, b1, b2, b3, b4, b18, b19, sess):
    b11 = tf.global_variables_initializer()
    sess.run(b11)
    for step in range(2017):
        sess.run(b10, b12 = {b3: b1, b4: b2})
        if step % b13 = = 0:
            b14 = sess.run(b18, b12={b3: b1, b4: b2})
            b19.add_summary(b14, step)
            print(step, sess.run(b5), sess.run(b6))
def fonk7(sess, b3, b7):
    b12 = {b3: [10, b13, 40]}
    b15 = sess.run(b7, b12)
    print("Prediction:", b15)
def fonk8(sess, b20):
    b16 = b20.save(sess, "output/save.ckpt")
    print("Model saved in path:", b16)
def fonk9():
    print("=== TensorFlow Linear b17 = ==")
    b1, b2 = fonk1()
    b3, b4 = fonk2()
    b7 = fonk3(b3, b4)
    b8 = fonk4(b7, b4)
    b10 = fonk5(b8)
    with tf.Session() as sess:
        b18 = tf.summary.merge_all()
        b19 = tf.summary.FileWriter("logs/", sess.graph)
        fonk6(b10, b1, b2, b3, b4, b18, b19, sess)
        fonk7(sess, b3, b7)
        b20 = tf.train.Saver()
        fonk8(sess, b20)
if b21 = = '__main__':
    fonk9()