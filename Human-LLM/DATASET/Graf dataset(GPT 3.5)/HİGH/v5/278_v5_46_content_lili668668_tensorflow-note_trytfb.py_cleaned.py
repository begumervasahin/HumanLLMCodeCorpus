import tensorflow as tf
import numpy as np
def fonk1(b1 = 100):
    b2 = np.random.rand(b1).astype(np.float32)
    b3 = b2 * 0.1 + 0.3
    return b2, b3
def fonk2(x):
    with tf.name_scope('layer'):
        with tf.name_scope('b4'):
            b4 = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="W")
            tf.summary.histogram('b4', b4)
        with tf.name_scope('b5'):
            b5 = tf.Variable(tf.zeros([1]), name="b")
            tf.summary.histogram('b5', b5)
        with tf.name_scope('Wx_add_b'):
            b6 = b4 * x + b5
    return b6
def fonk3(b11, b12, b6):
    with tf.name_scope('b7'):
        b7 = tf.reduce_mean(tf.square(b6 - b12))
        tf.summary.scalar('b7', b7)
    with tf.name_scope('b9'):
        b8 = tf.b9.GradientDescentOptimizer(0.5)
        b9 = b8.minimize(b7)
    return b9, b7
def fonk4(sess, b14, b10):
    b10 = b14.save(sess, b10)
    print("Model saved in path: %s" % b10)
def fonk5():
    b2, b3 = fonk1()
    with tf.name_scope('inputs'):
        b11 = tf.placeholder(tf.float32, name='x_input')
        b12 = tf.placeholder(tf.float32, name='y_input')
    b6 = fonk2(b11)
    b9, b7 = fonk3(b11, b12, b6)
    b13 = tf.global_variables_initializer()
    b14 = tf.b9.Saver()
    with tf.Session() as sess:
        b15 = tf.summary.merge_all()
        b16 = tf.summary.FileWriter("logs/", sess.graph)
        sess.run(b13)
        for step in range(2017):
            sess.run(b9, b17 = {b11: b2, b12: b3})
            if step % b18 = = 0:
                b19 = sess.run(b15, b17={b11: b2, b12: b3})
                b16.add_summary(b19, step)
                print(step, sess.run(b4), sess.run(b5))
        b17 = {b11: [10, b18, 40]}
        b20 = sess.run(b6, b17)
        print(b20)
        fonk4(sess, b14, "output/save.ckpt")
if b21 = = "__main__":
    fonk5()