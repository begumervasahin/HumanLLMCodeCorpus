import gym
import sys
from VRRL import VRRL,montocarloevaluation,policy_neural_net,sgd,b13
import copy
from log import log
global b1
b1 = None
class class1:
    def fonk1(self):
        self.b2 = None
        self.b3 = None
        self.b4 = gym.make(b1)
    def fonk2(self):
        b5 = self.b4.reset()
        self.b3 = b5
        self.a1 = 0
        self.b6 = False
        return self.fonk3()
    def fonk3(self):
        return copy.deepcopy(self.b3)
    def fonk4(self,action):
        b5, reward, done, b7 = self.b4.a1(action)
        self.b3 = b5
        self.a1+=1
        if  self.b6 or done or self.a1 > self.b4.spec.timestep_limit:
            self.b6 = True
        else:
            self.b6 = False
        return self.fonk3(),float(reward)
    def fonk5(self):
        return self.b6
b8 = ['CartPole-v0','Acrobot-v1','MountainCar-v0','Pendulum-v0']
for k in b8:
    b1 = k
    for i in [True]:
        for j in [True,False]:
            b9 = gym.make(b1)
            b10 = b9.observation_space.shape[0]
            a2 = 16
            b11 = b9.action_space.n
            b12 = b9.spec.timestep_limit
            del(b9)
            a3 = 64
            b13 = a3
            b14 = [b10,8,8,b11]
            b15 = log(b1)
            b16 = policy_neural_net(b14,a3)
            b17 = montocarloevaluation(b15,a3=a3,baseline=i,vareduce=j)
            b18 = sgd(0.2)
            b19 = VRRL(b16,b17,b13,class1,b18)
            b19.train(2000)