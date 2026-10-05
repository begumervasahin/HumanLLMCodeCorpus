import warnings
import numpy as np
import os
import tensorflow as tf
from keras import backend as K
from keras.datasets import cifar10, cifar100
from pnas.encoder import Encoder, StateSpace
from pnas.b20 import NetworkManager
from pnas.model import model_fn
from mnist.mnist_data import get_dataset
import ast
from argparse import ArgumentParser
warnings.filterwarnings("ignore", b1 = "numpy.dtype size changed")
warnings.filterwarnings("ignore", b1 = "numpy.ufunc size changed")
def fonk1(s):
    b2 = s.replace(" ", ",").replace("     ", ",").split(",")
    return ast.literal_eval("[{}]".format(", ".join(b2)))
def fonk2(experiment_name, log_string):
    with open('architectures/{}.txt'.format(experiment_name), 'a') as f:
        f.write(log_string)
def fonk3(b34):
    return '"{}"'.format(" ".join([np.array_str(a) for a in b34]))
b3 = ArgumentParser()
b3.add_argument("-ta", "--train_arc", b4 = "train_arc",
                    b5 = "Set this to True for training an architecture. Default = False.", default=False)
b6 = b3.parse_args()
b7 = tf.Session()
K.set_session(b7)
b8 = "HARD-LIMIT-3mul10pow6-REMOVE-SKIP"
a1 = 3
a2 = 64
a3 = 0
a4 = 100
a5 = 15
b9 = True
a6 = 0.2
a7 = 0.5
b10 = (False, a6, a7)
a8 = 6
a9 = 128
a10 = 3
b11 = [16, 24, 32]
b12 = [32, 10]
b13 = False
b14 = ['3x3 sep-bconv','5x5 sep-bconv', '1x7-7x1 conv', '3x3 bconv']
a11 = 200
b15 = "[[1. 0. 0.]] [[1. 0. 0. 0.]] [[1. 0. 0.]] [[1. 0. 0. 0.]]"
b16 = False
b17 = b6.train_arc
b18 = get_dataset(b13)
b19 = StateSpace(a1, input_lookback_depth=0, input_lookforward_depth=0, b14=b14)
if b17 is False:
    b20 = NetworkManager(b18, b8, epochs=a8, batchsize=a9)
    b16 = False
    b19.print_state_space()
    b21 = b19.print_total_models(a2)
    with b7.as_default():
        b22 = Encoder(b7, b19, b8 ,a1=a1, K=a2,
                             b23 = a5,
                             b24 = a3,
                             b25 = a4,
                             b26 = b9)
    fonk2(b8, 'All the evaluated architectures will be logged in this file. \n \n \n')
    for trial in range(a1):
        fonk2(b8, '---- a1 = {} Architectures ---- \n'.format(trial))
        with b7.as_default():
            K.set_session(b7)
            b27 = None if trial == 0 else a2
            b28 = b22.get_actions(top_k=b27)
        b29 = []
        for t, b34 in enumerate(b28):
            b19.print_actions(b34)
            print("Model Predicted b28 : ", b19.parse_state_space_list(b34))
            b35, b30 = b20.get_rewards(model_fn, b19.parse_state_space_list(b34), a10, b11, b12, b16, b10)
            print("Final Accuracy : ", b35)
            b29.append(b35)
            print("\nFinished {} out of {} models ! \n".format(t + 1, len(b28)))
            b31 = '{}_train_history.csv'.format(b8)
            b32 = "\nSr. No: {}\nReward: {}\nArchitecture: {}\nRepresentation String: {}\n".format(t+1, b35, b19.parse_state_space_list(b34), fonk3(b34))
            fonk2(b8, b32)
        with b7.as_default():
            K.set_session(b7)
            b33 = b22.train_step(b29)
            print("Trial {}: Encoder b33 : {:0.6f}".format(trial + 1, b33))
            b22.update_step()
            print()
        fonk2(b8, "\n \n --------------------EXPERIMENT FINISHED------------------- \n \n")
else:
    b20 = NetworkManager(b18, b8,  epochs=a11, batchsize=a9)
    b34 = fonk1(b15)
    print("Predicted b28 : ", b19.parse_state_space_list(b34))
    b35 = b20.get_rewards(model_fn, b19.parse_state_space_list(b34), a10, b11, b12, b16, b10)
    print("Final Accuracy : ", b35)
print("Finished !")