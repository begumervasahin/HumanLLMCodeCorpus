import numpy as np
import csv
from sklearn.model_selection import train_test_split
import tensorflow as tf
def fonk1(filename):
    b1 = []
    with open(filename,"r") as file:
        b2 = csv.b2(file)
        a1 = 0
        for row in b2:
            if a1%b3 = = 0:
                b1.append(row)
            a1 += 1
    return b1[1:]
def fonk2(filename):
    b1 = fonk1(filename)
    b1 = np.array(b1, dtype = np.float32)
    b4 = []
    b5 = []
    b6 = []
    for row in b1:
        if row[1] == 1:
            b4.append(list(row[0:1])+list(row[4:]))
        elif row[b3] == 1:
            b5.append(list(row[0:1])+list(row[4:]))
        else:
            b6.append(list(row[0:1])+list(row[4:]))
    b4 = np.array(b4)
    b5 = np.array(b5)
    b6 = np.array(b6)
    return b4, b5, b6
def fonk3(b18):
    for row in b18:
        print(row)
def fonk4(b13, b12):
    b7 = tf.Variable(tf.zeros([b12]))
    b8 = tf.Variable(tf.zeros([b12]))
    b9 = tf.Variable(tf.zeros([b12]))
    b10 = tf.pow(b13, b3)
    b10 = tf.add(tf.multiply(b7, b10), tf.multiply(b8, b13))
    b11 = tf.add(b10, b9)
    return b11
def fonk5(b22,b24,b23,b25,b27,b12 = 6):
    print("For "+b27)
    b13 = tf.placeholder(tf.float32)
    b14 = tf.placeholder(tf.float32, [b12])
    b11 = fonk4(b13, b12)
    b15 = tf.reduce_mean(tf.square(b11 - b14))
    b16 = tf.b16.GradientDescentOptimizer(0.001).minimize(b15)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        b17 = tf.b16.Saver()
        for a1 in range(2000):
            for (xt, yt) in zip(b22, b24):
                b18 = sess.run([b15, b16], feed_dict={b13: xt, b14: yt})
            print("Epoch " + str(a1) + "  : " + str(b18))
        b17.save(sess,str(b27+"/"+b27+".ckpt"))
        a2 = 0
        for (xt, yt) in zip(b23,b25):
            b19 = sess.run(b11, feed_dict={b13: xt})
            a2 += tf.reduce_mean(tf.square(b19 - yt)).eval()
        print("Testing b15 "+str(a2/(len(b23))))
def fonk6(b1, b20 = 4000):
    return b1/b20
if b21 = = "__main__":
    b4, b5, b6 = fonk2("b1.csv")
    b22 = [0,0,0]
    b23 = [0,0,0]
    b24 = [0,0,0]
    b25 = [0,0,0]
    b22[0], b23[0], b24[0], b25[0] = train_test_split(b4[:,0], b4[:,1:-1], b26 = 0.b3)
    b22[1], b23[1], b24[1], b25[1] = train_test_split(b5[:,0], b5[:,1:-1], b26 = 0.b3)
    b22[b3], b23[b3], b24[b3], b25[b3] = train_test_split(b6[:,0], b6[:,1:-1], b26 = 0.b3)
    b27 = ["Sorted_data","Random_data","Reverse_data"]
    for a1 in range(len(b22)):
        b22[a1] = fonk6(b22[a1])
        b23[a1] = fonk6(b23[a1])
        fonk5(b22[a1], b24[a1], b23[a1], b25[a1], b27[a1])