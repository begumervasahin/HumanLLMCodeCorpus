import warnings
import os
import numpy as np
import tensorflow as tf
from keras import backend as K
from argparse import ArgumentParser
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
def get_dataset(use_expansion):
    print("Dataset loaded with expansion:", use_expansion)
    return None
class Encoder:
    def __init__(self, session, state_space, experiment_name, B, K, train_iterations, reg_param, controller_cells, restore_controller):
        print(f"Encoder initialized for {experiment_name}")
    def get_actions(self, top_k=None):
        print("Actions generated")
        return [[np.random.rand(3)] for _ in range(5)]
    def train_step(self, rewards):
        print("Training step completed")
        return np.random.rand()
    def update_step(self):
        print("Update step completed")
class StateSpace:
    def __init__(self, B, input_lookback_depth, input_lookforward_depth, operators):
        print("StateSpace initialized")
    def print_state_space(self):
        print("StateSpace printed")
    def print_total_models(self, K):
        print(f"Total models: {K}")
        return K
    def parse_state_space_list(self, action):
        print("StateSpace list parsed")
        return action
    def print_actions(self, action):
        print(f"Actions: {action}")
class NetworkManager:
    def __init__(self, dataset, experiment_name, epochs, batchsize):
        print(f"NetworkManager initialized for {experiment_name}")
    def get_rewards(self, model_fn, parsed_state_space, num_cells, num_cell_filters, dense_layers, load_saved, dropout):
        print("Rewards computed")
        return np.random.rand(), None
def model_fn():
    pass
def log_architecture(experiment_name, log_string):
    if not os.path.exists('architectures/'):
        os.makedirs('architectures/')
    log_file_path = f'architectures/{experiment_name}.txt'
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_string)
def get_action(s):
    return np.random.rand(3, 3).tolist()
def get_architecture_from_action(action):
    return str(action)
parser = ArgumentParser()
parser.add_argument("-ta", "--train_arc", dest="train_arc", action='store_true',
                    help="Set this to True for training an architecture. Default is False.")
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
OPERATORS = ['3x3 sep-bconv', '5x5 sep-bconv', '1x7-7x1 conv', '3x3 bconv']
NUM_EPOCHS = 200
REPRESENTATION_STRING = "[[1. 0. 0.]] [[1. 0. 0. 0.]] [[1. 0. 0.]] [[1. 0. 0. 0.]]"
LOAD_SAVED = False
TRAIN_ARCHITECTURE = args.train_arc
dataset = get_dataset(USE_EXPANSION)
state_space = StateSpace(B, input_lookback_depth=0, input_lookforward_depth=0, operators=OPERATORS)
if not TRAIN_ARCHITECTURE:
    manager = NetworkManager(dataset, EXPERIMENT_NAME, epochs=MAX_EPOCHS, batchsize=BATCHSIZE)
    state_space.print_state_space()
    NUM_TRAILS = state_space.print_total_models(K_)
    with policy_sess.as_default():
        controller = Encoder(policy_sess, state_space, EXPERIMENT_NAME, B=B, K=K_,
                             train_iterations=RNN_TRAINING_EPOCHS, reg_param=REGULARIZATION,
                             controller_cells=CONTROLLER_CELLS, restore_controller=RESTORE_CONTROLLER)
    log_architecture(EXPERIMENT_NAME, 'All the evaluated architectures will be logged in this file.\n\n\n')
    for trial in range(B):
        log_architecture(EXPERIMENT_NAME, f'---- B= {trial} Architectures ----\n')
        with policy_sess.as_default():
            K.set_session(policy_sess)
            actions = controller.get_actions(top_k=None if trial == 0 else K_)
        rewards = []
        for t, action in enumerate(actions):
            state_space.print_actions(action)
            parsed_action = state_space.parse_state_space_list(action)
            reward, _ = manager.get_rewards(model_fn, parsed_action, NUM_CELLS, NUM_CELL_FILTERS, DENSE_LAYERS, LOAD_SAVED, DROPOUT)
            rewards.append(reward)
            log_str = (f"\nSr. No: {t+1}\nReward: {reward}\nArchitecture: {parsed_action}\n"
                       f"Representation String: {get_architecture_from_action(action)}\n")
            log_architecture(EXPERIMENT_NAME, log_str)
        with policy_sess.as_default():
            K.set_session(policy_sess)
            loss = controller.train_step(rewards)
            controller.update_step()
            print(f"Trial {trial + 1}: Encoder loss: {loss:.6f}\n")
    log_architecture(EXPERIMENT_NAME, "\n\n--------------------EXPERIMENT FINISHED-------------------\n\n")
else:
    manager = NetworkManager(dataset, EXPERIMENT_NAME, epochs=NUM_EPOCHS, batchsize=BATCHSIZE)
    action = get_action(REPRESENTATION_STRING)
    parsed_action = state_space.parse_state_space_list(action)
    reward = manager.get_rewards(model_fn, parsed_action, NUM_CELLS, NUM_CELL_FILTERS, DENSE_LAYERS, LOAD_SAVED, DROPOUT)
    print(f"Final Accuracy: {reward}")
print("Finished!")