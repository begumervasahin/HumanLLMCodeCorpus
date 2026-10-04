import numpy as np
import copy
import random
from keras.models import load_model
import keras
BUFFER_LENGTH = 10
MAX_STEP = 20
class Environment:
    def __init__(self):
        self.action_space = np.zeros((2,))
        self.observation_space = np.zeros((BUFFER_LENGTH * 2,))
        self.task_space = np.zeros((2,))
def action_to_readable(action):
    coordinate = np.random.choice(len(action[0]), 1, p=action[0])[0]
    return coordinate
class RNNModel:
    def __init__(self):
        self.model = load_model('trained_RNN')
        self.model.compile(loss='mse', optimizer='adam')
    def state_to_input(self, state):
        res = copy.deepcopy(state)
        for sublist in res:
            sublist = [x + 1 for x in sublist]
            sublist.extend([0] * (BUFFER_LENGTH - len(sublist)))
        return [res[0], res[1]]
    def state_to_RNN_input(self, state):
        temp = self.state_to_input(state)
        temp[0].append(-1)
        temp[1].append(-1)
        padded = keras.preprocessing.sequence.pad_sequences(temp, MAX_STEP, dtype='float32', padding='post', value=-100)
        return padded[0], padded[1]
    def get_action(self, state, task):
        translated = self.state_to_RNN_input(state)
        return self.model.predict([translated[0].reshape(1, len(translated[0]), 1), translated[1].reshape(1, len(translated[1]), 1)])
class MLPModel:
    def __init__(self):
        self.model = load_model('model_a_3_8')
        self.model.compile(loss='mse', optimizer='adam')
    def state_to_MLP_input(self, state, separated=False):
        res = copy.deepcopy(state)
        for sublist in res:
            sublist = [x + 1 for x in sublist]
            sublist.extend([0] * (BUFFER_LENGTH - len(sublist)))
        if not separated:
            return np.array([res[0] + res[1]])
        else:
            return np.array([res[0], res[1]])
    def get_action(self, state, task):
        translated = self.state_to_MLP_input(state)
        return self.model.predict([translated, task])
    def get_action_segmentation(self, state, task):
        segmentation_length = 5
        translated = self.state_to_MLP_input(state, True)
        res = None
        for i in range(BUFFER_LENGTH
            seg1 = translated[0][i * segmentation_length: (i + 1) * segmentation_length]
            seg2 = translated[1][i * segmentation_length: (i + 1) * segmentation_length]
            action = self.model.predict([[list(seg1) + list(seg2)], task])
            res = res + action if res is not None else action
        return res / (BUFFER_LENGTH
    def get_action_sliding_window(self, state, task):
        segmentation_length = 5
        translated = self.state_to_MLP_input(state, True)
        res = None
        for i in range(BUFFER_LENGTH - segmentation_length + 1):
            seg1 = translated[0][i: i + segmentation_length]
            seg2 = translated[1][i: i + segmentation_length]
            action = self.model.predict([[list(seg1) + list(seg2)], task])
            res = res + action if res is not None else action
        return res / (BUFFER_LENGTH - segmentation_length + 1)
def initialize_state():
    return [[], []]
def state_to_input(state):
    res = copy.deepcopy(state)
    for sublist in res:
        sublist = [x + 1 for x in sublist]
        sublist.extend([0] * (BUFFER_LENGTH - len(sublist)))
    return np.array([res[0] + res[1]])
def working(state):
    A, B = 0, 1
    p0a, p0b = 0.5, 1
    if A in state[0]:
        p0b *= 0.5
    p1a, p1b = 0.6, 0.6
    if B not in state[1]:
        p1a *= 0.5
    cur_p = random.random()
    if state[0] and state[0][0] == A and cur_p < p0a:
        state[0].pop(0)
    elif state[0] and cur_p < p0b:
        state[0].pop(0)
    if state[1] and state[1][0] == A and cur_p < p1a:
        state[1].pop(0)
    elif state[1] and cur_p < p1b:
        state[1].pop(0)
def update_state_by_action(state, action, task):
    if len(state[action]) < BUFFER_LENGTH:
        state[action].append(task)
        return 1
    return 0
def task_to_matrix(task):
    res = [0, 0]
    res[task] = 1
    return np.array([res])
def main():
    model = MLPModel()
    random.seed()
    total_reward = 0
    test_rounds = 10000
    with open('evaluated.txt', 'w') as f:
        temp = 0
        for round in range(test_rounds):
            if round % 1000 == 0 and round != 0:
                print(temp / round)
            cur_state = initialize_state()
            I = 1.0
            total_reward = 0
            for ind in range(40):
                for task_ind in range(2):
                    new_task = random.randrange(2)
                    action = model.get_action(cur_state, task_to_matrix(new_task))
                    action_translated = action_to_readable(action[new_task] if len(action) > 1 else action)
                    if len(cur_state[action_translated]) >= BUFFER_LENGTH:
                        action_translated = 1 - action_translated
                    new_state = copy.deepcopy(cur_state)
                    reward = update_state_by_action(new_state, action_translated, new_task)
                    cur_state = new_state
                    total_reward += reward
                    if reward == 0:
                        break
                working(cur_state)
                if reward == 0:
                    break
            temp += total_reward
            f.write(f"{total_reward}\n")
    print('avg reward: ', temp / test_rounds)
if __name__ == "__main__":
    main()