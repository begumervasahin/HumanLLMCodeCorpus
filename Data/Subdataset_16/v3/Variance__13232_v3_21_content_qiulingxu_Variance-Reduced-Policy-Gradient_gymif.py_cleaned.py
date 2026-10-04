import gym
import copy
from VRRL import VRRL, montocarloevaluation, policy_neural_net, sgd
from log import log
class class1:
    def fonk1(self, env_name):
        self.b1 = gym.make(env_name)
        self.b2 = None
        self.a1 = 0
        self.b3 = False
    def fonk2(self):
        self.b2 = self.b1.reset()
        self.a1 = 0
        self.b3 = False
        return self.fonk3()
    def fonk3(self):
        return copy.deepcopy(self.b2)
    def fonk4(self, action):
        observation, reward, b3, b4 = self.b1.a1(action)
        self.b2 = observation
        self.a1 += 1
        self.b3 = b3 or self.a1 >= self.b1.spec.max_episode_steps
        return self.fonk3(), float(reward)
    def fonk5(self):
        return self.b3
def fonk6(env_name):
    b1 = gym.make(env_name)
    b5 = b1.observation_space.shape[0]
    b6 = b1.action_space.n
    a2 = 64
    b7 = [b5, 8, 8, b6]
    b8 = log(env_name)
    b9 = policy_neural_net(b7, a2)
    for baseline in [True]:
        for vareduce in [True, False]:
            b10 = montocarloevaluation(b8, a2=a2, baseline=baseline, vareduce=vareduce)
            b11 = sgd(0.2)
            b12 = class1(env_name)
            b13 = VRRL(b9, b10, a2, b12, b11)
            b13.train(2000)
if b14 = = "__main__":
    b15 = ['CartPole-v0', 'Acrobot-v1', 'MountainCar-v0', 'Pendulum-v0']
    for exp_name in b15:
        fonk6(exp_name)