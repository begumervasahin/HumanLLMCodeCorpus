import gym
import copy
from VRRL import VRRL, montocarloevaluation, policy_neural_net, sgd
from log import log
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = gym.make(b1)
        self.b3 = None
        self.a1 = 0
        self.b4 = False
    def fonk2(self):
        self.b3 = self.b2.reset()
        self.a1 = 0
        self.b4 = False
        return self.fonk3()
    def fonk3(self):
        return copy.deepcopy(self.b3)
    def fonk4(self, action):
        observation, reward, b4, b5 = self.b2.a1(action)
        self.b3 = observation
        self.a1 += 1
        self.b4 = b4 or self.a1 >= self.b2.spec.max_episode_steps
        return self.fonk3(), float(reward)
    def fonk5(self):
        return self.b4
def fonk6(b1):
    b2 = gym.make(b1)
    b6 = b2.observation_space.shape[0]
    b7 = b2.action_space.n
    a2 = 64
    b8 = [b6, 8, 8, b7]
    b9 = log(b1)
    b10 = policy_neural_net(b8, a2)
    for baseline in [True]:
        for vareduce in [True, False]:
            b11 = montocarloevaluation(b9, a2=a2, baseline=baseline, vareduce=vareduce)
            b12 = sgd(0.2)
            b13 = class1(b1)
            b14 = VRRL(b10, b11, a2, b13, b12)
            b14.train(2000)
if b15 = = "__main__":
    b16 = ['CartPole-v0', 'Acrobot-v1', 'MountainCar-v0', 'Pendulum-v0']
    for exp_name in b16:
        fonk6(exp_name)