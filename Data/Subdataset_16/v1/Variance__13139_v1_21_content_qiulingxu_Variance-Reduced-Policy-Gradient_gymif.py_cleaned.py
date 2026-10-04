import gym
import copy
from VRRL import VRRL, montocarloevaluation, policy_neural_net, sgd, bs1
from log import log
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = gym.make(b1)
        self.b3 = None
        self.b4 = None
        self.a1 = 0
        self.b5 = False
    def fonk2(self):
        self.b4 = self.b2.reset()
        self.a1 = 0
        self.b5 = False
        return self.fonk3()
    def fonk3(self):
        return copy.deepcopy(self.b4)
    def fonk4(self, action):
        observation, reward, done, b6 = self.b2.a1(action)
        self.b4 = observation
        self.a1 += 1
        if self.b5 or done or self.a1 > self.b2.spec.max_episode_steps:
            self.b5 = True
        else:
            self.b5 = False
        return self.fonk3(), float(reward)
    def fonk5(self):
        return self.b5
def fonk6(b1):
    b2 = gym.make(b1)
    b7 = b2.observation_space.shape[0]
    a2 = 16
    b8 = b2.action_space.n
    b9 = b2.spec.max_episode_steps
    a3 = 64
    b10 = [b7, 8, 8, b8]
    b11 = log(b1)
    b12 = policy_neural_net(b10, a3)
    for baseline in [True]:
        for vareduce in [True, False]:
            b13 = montocarloevaluation(b11, a3=a3, baseline=baseline, vareduce=vareduce)
            b14 = sgd(0.2)
            b15 = VRRL(b12, b13, a3, class1(b1), b14)
            b15.train(2000)
if b16 = = "__main__":
    b17 = ['CartPole-v0', 'Acrobot-v1', 'MountainCar-v0', 'Pendulum-v0']
    for exp_name in b17:
        fonk6(exp_name)