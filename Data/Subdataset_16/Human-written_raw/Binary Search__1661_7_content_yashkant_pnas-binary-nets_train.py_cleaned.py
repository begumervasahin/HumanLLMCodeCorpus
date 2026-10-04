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
from pnas.b22 import NetworkManager
from pnas.model import model_fn
from mnist.mnist_data import get_dataset
import ast
if not os.path.exists('architectures/'):
    os.makedirs('architectures/')
def fonk1(s):
    b2 = ""
    for i in range(len(s)):
        if(s[i] == " " or s[i] == "	"):
            b2+=","
        else:
            b2+= s[i]
    print(b2)
    return ast.literal_eval("[ " + b2 + " ]")
def fonk2(experiment_name, log_string):
    b3 = open('architectures/' + experiment_name + '.txt','a')
    b3.write(log_string)
    b3.close()
def fonk3(b37):
    b4 = ""
    for i in range(len(b37)):
        b4 += np.array_str(b37[i]) + " "
    return '"' + b4[:-1] + '"'
from argparse import ArgumentParser
b5 = ArgumentParser()
b5.add_argument("-ta", "--train_arc", b6 = "train_arc",
                    b7 = "Set this to True for training an architecture. Default = False.", default = False)
b8 = b5.parse_args()
b9 = tf.Session()
K.set_session(b9)
b10 = "HARD-LIMIT-3mul10pow6-REMOVE-SKIP"
a1 = 3
a2 = 64
a3 = 0
a4 = 100
a5 = 15
b11 = True
a6 = 0.2
a7 = 0.5
b12 = (False, a6, a7)
a8 = 6
a9 = 128
a10 = 3
b13 = [16, 24, 32]
b14 = [32, 10]
b15 = False
b16 = ['3x3 sep-bconv','5x5 sep-bconv', '1x7-7x1 conv',
              '3x3 bconv']
a11 = 200
b17 = "[[1. 0. 0.]] [[1. 0. 0. 0.]] [[1. 0. 0.]] [[1. 0. 0. 0.]]"
b18 = False
b19 = b8.train_arc
b20 = get_dataset(b15)
b21 = StateSpace(a1, input_lookback_depth=0, input_lookforward_depth=0,
                         b16 = b16)
if(b19 is False):
    b22 = NetworkManager(b20, b10,  epochs=a8, batchsize=a9)
    b18 = False
    b21.print_state_space()
    b23 = b21.print_total_models(a2)
    with b9.as_default():
        b24 = Encoder(b9, b21, b10 ,a1=a1, K=a2,
                             b25 = a5,
                             b26 = a3,
                             b27 = a4,
                             b28 = b11)
    print()
    fonk2(b10, 'All the evaluated architectures will be logged in this file. \n \n \n')
    for b29 in range(a1):
        fonk2(b10, '---- a1 = ' + str(b29) + " Architectures ---- \n" )
        with b9.as_default():
            K.set_session(b9)
            if b29 = = 0:
                b30 = None
            else:
                b30 = a2
            b31 = b24.get_actions(top_k=b30)
        b32 = []
        for t, b37 in enumerate(b31):
            b21.print_actions(b37)
            print("Model
            print("Predicted b31 : ", b21.parse_state_space_list(b37))
            b38, b33 = b22.get_rewards(model_fn, b21.parse_state_space_list(b37), a10, b13, b14, b18, b12)
            print("Final Accuracy : ", b38)
            b32.append(b38)
            print("\nFinished %d out of %d models ! \n" % (t + 1, len(b31)))
            b34 = b10 + '_train_history.csv'
            b35 = "\nSr. No: " + str(t+1)+ "\nReward: " + str(b38) + "\nArchitecture: " + str(b21.parse_state_space_list(b37)) + "\nRepresentation String: " + fonk3(b37) + "\n"
            fonk2(b10, b35)
        with b9.as_default():
            K.set_session(b9)
            b36 = b24.train_step(b32)
            print("Trial %d: Encoder b36 : %0.6f" % (b29 + 1, b36))
            b24.update_step()
            print()
        fonk2(b10, "\n \n --------------------EXPERIMENT FINISHED------------------- \n \n")
else:
    b22 = NetworkManager(b20, b10,  epochs=a11, batchsize=a9)
    b37 = fonk1(b17)
    print("Predicted b31 : ", b21.parse_state_space_list(b37))
    b38 = b22.get_rewards(model_fn, b21.parse_state_space_list(b37), a10, b13, b14, b18, b12)
    print("Final Accuracy : ", b38)
print("Finished !")