import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
import numpy as np
import csv
import os
import tensorflow as tf
from keras import backend as K
from keras.datasets import cifar10, cifar100
from keras.utils import to_categorical
from argparse import ArgumentParser
from pnas.encoder import Encoder, StateSpace
from pnas.manager import NetworkManager
from pnas.model import model_fn
from mnist.mnist_data import get_dataset
import ast
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
if not os.path.exists('architectures/'):
    os.makedirs('architectures/')
def get_action(representation_string):
    formatted_string = ",".join(representation_string.split())
    print(formatted_string)
    return ast.literal_eval(f"[{formatted_string}]")
def log_architecture(experiment_name, log_string):
    with open(f'architectures/{experiment_name}.txt', 'a') as f:
        f.write(log_string)
def get_architecture_from_action(action):
    arc = " ".join(np.array_str(a) for a in action)
    return f'"{arc}"'
parser = ArgumentParser()
parser.add_argument("-ta", "--train_arc", dest="train_arc",
                    help="Set this to True for training an architecture. Default = False.",
                    default=False)
args = parser.parse_args()
policy_sess = tf.Session()
K.set_session(policy_sess)
EXPERIMENT_NAME = "HARD-LIMIT-3mul10pow6-REMOVE-SKIP"
B = 3
K_ = 64
REGULARIZATION = 0
CONTROLLER_CELLS = 100
RNN_TRAINING_EPOCHS = 15
RESTORE_CONTROLLER = True
DROP_INPUT = 0.2
DROP_HIDDEN = 0.5
DROPOUT = (False, DROP_INPUT, DROP_HIDDEN)
MAX_EPOCHS = 6
BATCHSIZE = 128
NUM_CELLS = 3
NUM_CELL_FILTERS = [16, 24, 32]
DENSE_LAYERS = [32, 10]
USE_EXPANSION = False
operators = ['3x3 sep-bconv', '5x5 sep-bconv', '1x7-7x1 conv', '3x3 bconv']
NUM_EPOCHS = 200
REPRESENTATION_STRING = "[[1. 0. 0.]] [[1. 0. 0. 0.]] [[1. 0. 0.]] [[1. 0. 0. 0.]]"
LOAD_SAVED = False
TRAIN_ARCHITECTURE = args.train_arc
dataset = get_dataset(USE_EXPANSION)
state_space = StateSpace(B, input_lookback_depth=0, input_lookforward_depth=0, operators=operators)
if not TRAIN_ARCHITECTURE:
    manager = NetworkManager(dataset, EXPERIMENT_NAME, epochs=MAX_EPOCHS, batchsize=BATCHSIZE)
    LOAD_SAVED = False
    state_space.print_state_space()
    NUM_TRIALS = state_space.print_total_models(K_)
    with policy_sess.as_default():
        controller = Encoder(policy_sess, state_space, EXPERIMENT_NAME, B=B, K=K_,
                             train_iterations=RNN_TRAINING_EPOCHS,
                             reg_param=REGULARIZATION,
                             controller_cells=CONTROLLER_CELLS,
                             restore_controller=RESTORE_CONTROLLER)
    print()
    log_architecture(EXPERIMENT_NAME, 'All the evaluated architectures will be logged in this file.\n\n\n')
    for trial in range(B):
        log_architecture(EXPERIMENT_NAME, f'---- B= {trial} Architectures ---- \n')
        with policy_sess.as_default():
            K.set_session(policy_sess)
            k = None if trial == 0 else K_
            actions = controller.get_actions(top_k=k)
        rewards = []
        for t, action in enumerate(actions):
            state_space.print_actions(action)
            print(f"Model {t + 1}")
            print("Predicted actions: ", state_space.parse_state_space_list(action))
            reward, mul_ops = manager.get_rewards(
                model_fn, state_space.parse_state_space_list(action),
                NUM_CELLS, NUM_CELL_FILTERS, DENSE_LAYERS, LOAD_SAVED, DROPOUT
            )
            print("Final Accuracy: ", reward)
            rewards.append(reward)
            print(f"\nFinished {t + 1} out of {len(actions)} models!\n")
            train_hist_name = f'{EXPERIMENT_NAME}_train_history.csv'
            log_str = f"\nSr. No: {t + 1}\nReward: {reward}\nArchitecture: {state_space.parse_state_space_list(action)}\nRepresentation String: {get_architecture_from_action(action)}\n"
            log_architecture(EXPERIMENT_NAME, log_str)
        with policy_sess.as_default():
            K.set_session(policy_sess)
            loss = controller.train_step(rewards)
            print(f"Trial {trial + 1}: Encoder loss: {loss:.6f}")
            controller.update_step()
            print()
        log_architecture(EXPERIMENT_NAME, "\n\n--------------------EXPERIMENT FINISHED-------------------\n\n")
else:
    manager = NetworkManager(dataset, EXPERIMENT_NAME, epochs=NUM_EPOCHS, batchsize=BATCHSIZE)
    action = get_action(REPRESENTATION_STRING)
    print("Predicted actions: ", state_space.parse_state_space_list(action))
    reward = manager.get_rewards(
        model_fn, state_space.parse_state_space_list(action),
        NUM_CELLS, NUM_CELL_FILTERS, DENSE_LAYERS, LOAD_SAVED, DROPOUT
    )
    print("Final Accuracy: ", reward)
print("Finished!")