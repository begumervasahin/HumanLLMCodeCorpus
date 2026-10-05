import numpy as np
import copy
import random
from keras.models import load_model
BUFFER_LENGTH = 10
class MLPModel:
    def __init__(self):
        self.model = load_model('model_a_3_8')
        self.model.compile(loss='mse', optimizer='adam')
    def state_to_MLP_input(self, state, separated=False):
        res = copy.deepcopy(state)
        for i in range(len(res)):
            res[i] = [val + 1 for val in res[i]]
            while len(res[i]) < BUFFER_LENGTH:
                res[i].append(0)
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
            action = self.model.predict([[*seg1, *seg2], task])
            if res is not None:
                res += action
            else:
                res = action
        return res / (BUFFER_LENGTH
    def get_action_sliding_window(self, state, task):
        segmentation_length = 5
        translated = self.state_to_MLP_input(state, True)
        res = None
        for i in range(BUFFER_LENGTH - segmentation_length + 1):
            seg1 = translated[0][i: i + segmentation_length]
            seg2 = translated[1][i: i + segmentation_length]
            action = self.model.predict([[*seg1, *seg2], task])
            if res is not None:
                res += action
            else:
                res = action
        return res / (BUFFER_LENGTH - segmentation_length + 1)
def action_to_readable(action):
    coordinate = np.random.choice(len(action[0]), 1, p=action[0])[0]
    return coordinate
def initialize_state():
    return [[], []]
def working(state):
    A = 0
    B = 1
    p0a = 0.5
    p0b = 1
    if A in state[0]:
        p0b *= 0.5
    p1a = 0.6
    p1b = 0.6
    if B not in state[1]:
        p1a *= 0.5
    curP = random.random()
    if len(state[0]) > 0:
        if state[0][0] == A:
            if curP < p0a:
                state[0].pop(0)
        else:
            if curP < p0b:
                state[0].pop(0)
    if len(state[1]) > 0:
        if state[1][0] == A:
            if curP < p1a:
                state[1].pop(0)
        else:
            if curP < p1b:
                state[1].pop(0)
def update_state_by_action(state, action, task):
    if len(state[action]) >= BUFFER_LENGTH:
        return 0
    else:
        state[action].append(task)
        return 1
def task_to_matrix(task):
    res = [0, 0]
    res[task] = 1
    return np.array([res])
def main():
    model = MLPModel()
    random.seed()
    total_reward = 0
    with open('evaluated.txt', 'w') as f:
        temp = 0
        test_round = 10000
        for round in range(test_round):
            if round % 1000 == 0 and round != 0:
                print(temp / round)
            cur_state = initialize_state()
            total_reward = 0
            for ind in range(40):
                for task_ind in range(2):
                    new_task = random.randrange(2)
                    action = model.get_action(cur_state, task_to_matrix(new_task))
                    if len(action) > 1:
                        action_translated = action_to_readable(action[new_task])
                    else:
                        action_translated = action_to_readable(action)
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
            f.write(str(total_reward))
            f.write('\n')
    print('avg reward: ', temp / test_round)
if __name__ == "__main__":
    main()