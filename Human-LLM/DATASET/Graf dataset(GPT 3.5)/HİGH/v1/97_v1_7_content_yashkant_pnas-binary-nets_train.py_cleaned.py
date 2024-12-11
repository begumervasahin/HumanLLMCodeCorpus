import warnings
warnings.filterwarnings("ignore", b1 = "numpy.dtype size changed")
warnings.filterwarnings("ignore", b1 = "numpy.ufunc size changed")
import numpy as np
import csv
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
import tensorflow as tf
from keras import backend as K
from keras.datasets import cifar10, cifar100
from keras.utils import to_categorical
from pnas.encoder import Encoder, StateSpace
from pnas.b21 import NetworkManager
from pnas.model import model_fn
from mnist.mnist_data import get_dataset
import ast
from argparse import ArgumentParser
def fonk1(s):
    b2 = ""
    for i in range(len(s)):
        if s[i] == " " or s[i] == "     ":
            b2 += ","
        else:
            b2 += s[i]
    return ast.literal_eval("[ " + b2 + " ]")
def fonk2(experiment_name, log_string):
    with open('architectures/' + experiment_name + '.txt', 'a') as f:
        f.write(log_string)
def fonk3(b36):
    b3 = ""
    for i in range(len(b36)):
        b3 += np.array_str(b36[i]) + " "
    return '"' + b3[:-1] + '"'
b4 = ArgumentParser()
b4.add_argument("-ta", "--train_arc", b5 = "train_arc",
                    b6 = "Set this to True for training an architecture. Default = False.", default=False)
b7 = b4.parse_args()
b8 = tf.Session()
K.set_session(b8)
b9 = "HARD-LIMIT-3mul10pow6-REMOVE-SKIP"
a1 = 3
a2 = 64
a3 = 0
a4 = 100
a5 = 15
b10 = True
a6 = 0.2
a7 = 0.5
b11 = (False, a6, a7)
a8 = 6
a9 = 128
a10 = 3
b12 = [16, 24, 32]
b13 = [32, 10]
b14 = False
b15 = ['3x3 sep-bconv','5x5 sep-bconv', '1x7-7x1 conv', '3x3 bconv']
a11 = 200
b16 = "[[1. 0. 0.]] [[1. 0. 0. 0.]] [[1. 0. 0.]] [[1. 0. 0. 0.]]"
b17 = False
b18 = b7.train_arc
b19 = get_dataset(b14)
b20 = StateSpace(a1, input_lookback_depth=0, input_lookforward_depth=0, b15=b15)
if b18 is False:
    b21 = NetworkManager(b19, b9, epochs=a8, batchsize=a9)
    b17 = False
    b20.print_state_space()
    b22 = b20.print_total_models(a2)
    with b8.as_default():
        b23 = Encoder(b8, b20, b9 ,a1=a1, K=a2,
                             b24 = a5,
                             b25 = a3,
                             b26 = a4,
                             b27 = b10)
    fonk2(b9, 'All the evaluated architectures will be logged in this file. \n \n \n')
    for b28 in range(a1):
        fonk2(b9, '---- a1 = ' + str(b28) + " Architectures ---- \n" )
        with b8.as_default():
            K.set_session(b8)
            if b28 = = 0:
                b29 = None
            else:
                b29 = a2
            b30 = b23.get_actions(top_k=b29)
        b31 = []
        for t, b36 in enumerate(b30):
            b20.print_actions(b36)
            print("Model Predicted b30 : ", b20.parse_state_space_list(b36))
            b37, b32 = b21.get_rewards(model_fn, b20.parse_state_space_list(b36), a10, b12, b13, b17, b11)
            print("Final Accuracy : ", b37)
            b31.append(b37)
            print("\nFinished %d out of %d models ! \n" % (t + 1, len(b30)))
            b33 = b9 + '_train_history.csv'
            b34 = "\nSr. No: " + str(t+1)+ "\nReward: " + str(b37) + "\nArchitecture: " + str(b20.parse_state_space_list(b36)) + "\nRepresentation String: " + fonk3(b36) + "\n"
            fonk2(b9, b34)
        with b8.as_default():
            K.set_session(b8)
            b35 = b23.train_step(b31)
            print("Trial %d: Encoder b35 : %0.6f" % (b28 + 1, b35))
            b23.update_step()
            print()
        fonk2(b9, "\n \n --------------------EXPERIMENT FINISHED------------------- \n \n")
else:
    b21 = NetworkManager(b19, b9,  epochs=a11, batchsize=a9)
    b36 = fonk1(b16)
    print("Predicted b30 : ", b20.parse_state_space_list(b36))
    b37 = b21.get_rewards(model_fn, b20.parse_state_space_list(b36), a10, b12, b13, b17, b11)
    print("Final Accuracy : ", b37)
print("Finished !")