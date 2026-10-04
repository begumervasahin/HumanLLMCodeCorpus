import tensorflow as tf
import numpy as np
b1 = np.random.rand(100).astype(np.float32)
b2 = b1 * 0.1 + 0.3
def fonk1():
    with tf.name_scope('inputs'):
        b3 = tf.placeholder(tf.float32, name='x_input')
        b4 = tf.placeholder(tf.float32, name='y_input')
    with tf.name_scope('layer'):
        with tf.name_scope('b5'):
            b5 = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="W")
            tf.b13.histogram('b5', b5)
        with tf.name_scope('b6'):
            b6 = tf.Variable(tf.zeros([1]), name="b")
            tf.b13.histogram('b6', b6)
        with tf.name_scope('Wx_plus_b'):
            b7 = b5 * b3 + b6
    with tf.name_scope('b8'):
        b8 = tf.reduce_mean(tf.square(b7 - b4))
        tf.b13.scalar('b8', b8)
    with tf.name_scope('train'):
        b9 = tf.train.GradientDescentOptimizer(0.5)
        b10 = b9.minimize(b8)
    return b3, b4, b7, b5, b6, b8, b10
def fonk2(b3, b4, b10, b20, b21):
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for step in range(2017):
            sess.run(b10, b11 = {b3: b1, b4: b2})
            if step % b12 = = 0:
                b13 = sess.run(b20, b11={b3: b1, b4: b2})
                b21.add_summary(b13, step)
                current_weights, b14 = sess.run([b5, b6])
                print(f"Step {step}: b15 = {current_weights}, Biases = {b14}")
        return sess
def fonk3(sess, b3, b7, b22):
    b16 = sess.run(b7, b11={b3: b22})
    print("Predictions:", b16)
def fonk4(sess, b19, path):
    b17 = b19.save(sess, path)
    print(f"Model saved in path: {b17}")
if b18 = = "__main__":
    tf.reset_default_graph()
    b3, b4, b7, b5, b6, b8, b10 = fonk1()
    b19 = tf.train.Saver()
    b20 = tf.b13.merge_all()
    b21 = tf.b13.FileWriter("logs/", tf.get_default_graph())
    with fonk2(b3, b4, b10, b20, b21) as sess:
        b22 = [10, b12, 40]
        fonk3(sess, b3, b7, b22)
        fonk4(sess, b19, "output/save.ckpt")