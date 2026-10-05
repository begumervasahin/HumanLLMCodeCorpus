import warnings
import numpy as np
import os
import tensorflow as tf
from keras import backend as K
from keras.datasets import cifar10, cifar100
from pnas.encoder import Encoder, StateSpace
from pnas.b19 import NetworkManager
from pnas.model import model_fn
from mnist.mnist_data import get_dataset
import ast
from argparse import ArgumentParser
def fonk1(s):
    b1 = s.replace(" ", ",").replace("     ", ",").split(",")
    return ast.literal_eval("[{}]".format(", ".join(b1)))
def fonk2(experiment_name, log_string):
    with open('architectures/{}.txt'.format(experiment_name), 'a') as f:
        f.write(log_string)
def fonk3(b33):
    return '"{}"'.format(" ".join([np.array_str(a) for a in b33]))
b2 = ArgumentParser()
b2.add_argument("-ta", "--train_arc", b3 = "train_arc",
                    b4 = "Set this to True for training an architecture. Default = False.", default=False)
b5 = b2.parse_args()
b6 = tf.Session()
K.set_session(b6)
b7 = "HARD-LIMIT-3mul10pow6-REMOVE-SKIP"
a1 = 3
a2 = 64
a3 = 0
a4 = 100
a5 = 15
b8 = True
a6 = 0.2
a7 = 0.5
b9 = (False, a6, a7)
a8 = 6
a9 = 128
a10 = 3
b10 = [16, 24, 32]
b11 = [32, 10]
b12 = False
b13 = ['3x3 sep-bconv','5x5 sep-bconv', '1x7-7x1 conv', '3x3 bconv']
a11 = 200
b14 = "[[1. 0. 0.]] [[1. 0. 0. 0.]] [[1. 0. 0.]] [[1. 0. 0. 0.]]"
b15 = False
b16 = b5.train_arc
b17 = get_dataset(b12)
b18 = StateSpace(a1, input_lookback_depth=0, input_lookforward_depth=0, b13=b13)
if b16 is False:
    b19 = NetworkManager(b17, b7, epochs=a8, batchsize=a9)
    b15 = False
    b18.print_state_space()
    b20 = b18.print_total_models(a2)
    with b6.as_default():
        b21 = Encoder(b6, b18, b7 ,a1=a1, K=a2,
                             b22 = a5,
                             b23 = a3,
                             b24 = a4,
                             b25 = b8)
    fonk2(b7, 'All the evaluated architectures will be logged in this file. \n \n \n')
    for trial in range(a1):
        fonk2(b7, '---- a1 = {} Architectures ---- \n'.format(trial))
        with b6.as_default():
            K.set_session(b6)
            b26 = None if trial == 0 else a2
            b27 = b21.get_actions(top_k=b26)
        b28 = []
        for t, b33 in enumerate(b27):
            b18.print_actions(b33)
            print("Model Predicted b27 : ", b18.parse_state_space_list(b33))
            b34, b29 = b19.get_rewards(model_fn, b18.parse_state_space_list(b33), a10, b10, b11, b15, b9)
            print("Final Accuracy : ", b34)
            b28.append(b34)
            print("\nFinished {} out of {} models ! \n".format(t + 1, len(b27)))
            b30 = '{}_train_history.csv'.format(b7)
            b31 = "\nSr. No: {}\nReward: {}\nArchitecture: {}\nRepresentation String: {}\n".format(t+1, b34, b18.parse_state_space_list(b33), fonk3(b33))
            fonk2(b7, b31)
        with b6.as_default():
            K.set_session(b6)
            b32 = b21.train_step(b28)
            print("Trial {}: Encoder b32 : {:0.6f}".format(trial + 1, b32))
            b21.update_step()
            print()
        fonk2(b7, "\n \n --------------------EXPERIMENT FINISHED------------------- \n \n")
else:
    b19 = NetworkManager(b17, b7,  epochs=a11, batchsize=a9)
    b33 = fonk1(b14)
    print("Predicted b27 : ", b18.parse_state_space_list(b33))
    b34 = b19.get_rewards(model_fn, b18.parse_state_space_list(b33), a10, b10, b11, b15, b9)
    print("Final Accuracy : ", b34)
print("Finished !")