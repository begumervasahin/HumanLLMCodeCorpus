import warnings
warnings.filterwarnings("ignore", b1 = "numpy.dtype size changed")
warnings.filterwarnings("ignore", b1 = "numpy.ufunc size changed")
import numpy as np
import csv
import os
import tensorflow as tf
from keras import backend as K
from keras.datasets import cifar10, cifar100
from keras.utils import to_categorical
from argparse import ArgumentParser
from pnas.encoder import Encoder, StateSpace
from pnas.b22 import NetworkManager
from pnas.model import model_fn
from mnist.mnist_data import get_dataset
import ast
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
if not os.path.exists('architectures/'):
    os.makedirs('architectures/')
def fonk1(representation_string):
    b2 = ",".join(representation_string.split())
    print(b2)
    return ast.literal_eval(f"[{b2}]")
def fonk2(experiment_name, log_string):
    with open(f'architectures/{experiment_name}.txt', 'a') as f:
        f.write(log_string)
def fonk3(b36):
    b3 = " ".join(np.array_str(a) for a in b36)
    return f'"{b3}"'
b4 = ArgumentParser()
b4.add_argument("-ta", "--train_arc", b5 = "train_arc",
                    b6 = "Set this to True for training an architecture. Default = False.",
                    b7 = False)
b8 = b4.parse_args()
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
b16 = ['3x3 sep-bconv', '5x5 sep-bconv', '1x7-7x1 conv', '3x3 bconv']
a11 = 200
b17 = "[[1. 0. 0.]] [[1. 0. 0. 0.]] [[1. 0. 0.]] [[1. 0. 0. 0.]]"
b18 = False
b19 = b8.train_arc
b20 = get_dataset(b15)
b21 = StateSpace(a1, input_lookback_depth=0, input_lookforward_depth=0, b16=b16)
if not b19:
    b22 = NetworkManager(b20, b10, epochs=a8, batchsize=a9)
    b18 = False
    b21.print_state_space()
    b23 = b21.print_total_models(a2)
    with b9.as_default():
        b24 = Encoder(b9, b21, b10, a1=a1, K=a2,
                             b25 = a5,
                             b26 = a3,
                             b27 = a4,
                             b28 = b11)
    print()
    fonk2(b10, 'All the evaluated architectures will be logged in this file.\n\n\n')
    for trial in range(a1):
        fonk2(b10, f'---- a1 = {trial} Architectures ---- \n')
        with b9.as_default():
            K.set_session(b9)
            b29 = None if trial == 0 else a2
            b30 = b24.get_actions(top_k=b29)
        b31 = []
        for t, b36 in enumerate(b30):
            b21.print_actions(b36)
            print(f"Model {t + 1}")
            print("Predicted b30: ", b21.parse_state_space_list(b36))
            b37, b32 = b22.get_rewards(
                model_fn, b21.parse_state_space_list(b36),
                a10, b13, b14, b18, b12
            )
            print("Final Accuracy: ", b37)
            b31.append(b37)
            print(f"\nFinished {t + 1} out of {len(b30)} models!\n")
            b33 = f'{b10}_train_history.csv'
            b34 = f"\nSr. No: {t + 1}\nReward: {b37}\nArchitecture: {b21.parse_state_space_list(b36)}\nRepresentation String: {fonk3(b36)}\n"
            fonk2(b10, b34)
        with b9.as_default():
            K.set_session(b9)
            b35 = b24.train_step(b31)
            print(f"Trial {trial + 1}: Encoder b35: {b35:.6f}")
            b24.update_step()
            print()
        fonk2(b10, "\n\n--------------------EXPERIMENT FINISHED-------------------\n\n")
else:
    b22 = NetworkManager(b20, b10, epochs=a11, batchsize=a9)
    b36 = fonk1(b17)
    print("Predicted b30: ", b21.parse_state_space_list(b36))
    b37 = b22.get_rewards(
        model_fn, b21.parse_state_space_list(b36),
        a10, b13, b14, b18, b12
    )
    print("Final Accuracy: ", b37)
print("Finished!")