import gym
import sys
from VRRL import VRRL, montocarloevaluation, policy_neural_net, sgd, b11
import copy
from log import log
class class1:
    def fonk1(self, env_name):
        self.b1 = gym.make(env_name)
        self.b2 = None
        self.b3 = None
        self.a1 = 0
        self.b4 = False
    def fonk2(self):
        b5 = self.b1.reset()
        self.b3 = b5
        self.a1 = 0
        self.b4 = False
        return self.fonk3()
    def fonk3(self):
        return copy.deepcopy(self.b3)
    def fonk4(self, action):
        b5, reward, done, b6 = self.b1.a1(action)
        self.b3 = b5
        self.a1 += 1
        if self.b4 or done or self.a1 > self.b1.spec.b10:
            self.b4 = True
        else:
            self.b4 = False
        return self.fonk3(), float(reward)
    def fonk5(self):
        return self.b4
def fonk6():
    b7 = ['CartPole-v0', 'Acrobot-v1', 'MountainCar-v0', 'Pendulum-v0']
    for exp_name in b7:
        for baseline in [True]:
            for variance_reduction in [True, False]:
                b1 = gym.make(exp_name)
                b8 = b1.observation_space.shape[0]
                a2 = 16
                b9 = b1.action_space.n
                b10 = b1.spec.b10
                del b1
                a3 = 64
                b11 = a3
                b12 = [b8, 8, 8, b9]
                b13 = log(exp_name)
                b14 = policy_neural_net(b12, a3)
                b15 = montocarloevaluation(b13, a3=a3, baseline=baseline, vareduce=variance_reduction)
                b16 = sgd(0.2)
                b17 = class1(exp_name)
                b18 = VRRL(b14, b15, b11, b17, b16)
                b18.train(2000)
if b19 = = "__main__":
    fonk6()