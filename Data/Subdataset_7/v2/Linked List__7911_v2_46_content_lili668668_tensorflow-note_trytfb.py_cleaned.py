import tensorflow as tf
import numpy as np
b1 = np.random.rand(100).astype(np.float32)
b2 = b1 * 0.1 + 0.3
with tf.name_scope('inputs'):
    b3 = tf.placeholder(tf.float32, name='b3')
    b4 = tf.placeholder(tf.float32, name='b4')
with tf.name_scope('layer'):
    with tf.name_scope('b5'):
        b5 = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="W")
        tf.summary.histogram('b5', b5)
    with tf.name_scope('b6'):
        b6 = tf.Variable(tf.zeros([1]), name="b")
        tf.summary.histogram('b6', b6)
    with tf.name_scope('Wx_plus_b'):
        b7 = b5 * b3 + b6
with tf.name_scope('b8'):
    b8 = tf.reduce_mean(tf.square(b7 - b4))
    tf.summary.scalar('b8', b8)
with tf.name_scope('train'):
    b9 = tf.train.GradientDescentOptimizer(0.5)
    b10 = b9.minimize(b8)
b11 = tf.global_variables_initializer()
b12 = tf.train.Saver()
with tf.Session() as sess:
    b13 = tf.summary.merge_all()
    b14 = tf.summary.FileWriter("logs/", sess.graph)
    sess.run(b11)
    for step in range(2017):
        sess.run(b10, b15 = {b3: b1, b4: b2})
        if step % b16 = = 0:
            b17 = sess.run(b13, b15={b3: b1, b4: b2})
            b14.add_summary(b17, step)
            print(step, sess.run(b5), sess.run(b6))
    b15 = {b3: [10, b16, 40]}
    b18 = sess.run(b7, b15)
    print("Prediction:", b18)
    b19 = b12.save(sess, "output/save.ckpt")
    print("Model saved in path:", b19)