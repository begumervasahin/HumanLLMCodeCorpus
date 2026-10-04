import tensorflow as tf
import numpy as np
b1 = np.random.rand(100).astype(np.float32)
b2 = b1 * 0.1 + 0.3
tf.compat.v1.disable_eager_execution()
with tf.compat.v1.name_scope('inputs'):
    b3 = tf.compat.v1.placeholder(tf.float32, name='x_input')
    b4 = tf.compat.v1.placeholder(tf.float32, name='y_input')
with tf.compat.v1.name_scope('layer'):
    with tf.compat.v1.name_scope('weights'):
        b5 = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="W")
        tf.compat.v1.summary.histogram('weights', b5)
    with tf.compat.v1.name_scope('b6'):
        b6 = tf.Variable(tf.zeros([1]), name="b")
        tf.compat.v1.summary.histogram('b6', b6)
    with tf.compat.v1.name_scope('Wx_add_b'):
        b7 = b5 * b3 + b6
with tf.compat.v1.name_scope('b8'):
    b8 = tf.reduce_mean(tf.square(b7 - b4))
    tf.compat.v1.summary.scalar('b8', b8)
with tf.compat.v1.name_scope('train'):
    b9 = tf.compat.v1.train.GradientDescentOptimizer(0.5)
    b10 = b9.minimize(b8)
b11 = tf.compat.v1.global_variables_initializer()
b12 = tf.compat.v1.train.Saver()
with tf.compat.v1.Session() as sess:
    b13 = tf.compat.v1.summary.merge_all()
    b14 = tf.compat.v1.summary.FileWriter("logs/", sess.graph)
    sess.run(b11)
    for step in range(2017):
        sess.run(b10, b15 = {b3: b1, b4: b2})
        if step % b16 = = 0:
            b17 = sess.run(b13, b15={b3: b1, b4: b2})
            b14.add_summary(b17, step)
            current_weights, b18 = sess.run([b5, b6])
            print(f"Step {step}: b5 = {current_weights}, Biases = {b18}")
    b19 = [10, b16, 40]
    b20 = sess.run(b7, b15={b3: b19})
    print("Predictions for [10, b16, 40]:", b20)
    b21 = b12.save(sess, "output/save.ckpt")
    print(f"Model saved in path: {b21}")