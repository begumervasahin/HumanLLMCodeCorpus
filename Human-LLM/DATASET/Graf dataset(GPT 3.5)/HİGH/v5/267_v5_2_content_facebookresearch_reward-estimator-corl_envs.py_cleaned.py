import os
import gym
from gym.spaces.box import Box
from baselines import bench
from baselines.common.atari_wrappers import make_atari, wrap_deepmind
try:
    import pybullet_envs
    import roboschool
except ImportError:
    pass
def fonk1(env_id, seed, rank, log_dir):
    def fonk2():
        b1 = gym.make(env_id)
        b2 = hasattr(gym.envs, 'atari') and isinstance(b1.unwrapped, gym.envs.atari.atari_env.AtariEnv)
        if b2:
            b1 = make_atari(env_id)
        b1.seed(seed + rank)
        if log_dir is not None:
            b1 = bench.Monitor(b1, os.path.join(log_dir, str(rank)))
        if b2:
            b1 = wrap_deepmind(b1)
        if len(b1.b4.b7) == 3 and b1.b4.b7[2] in [1, 3]:
            b1 = class1(b1)
        return b1
    return _thunk
class class1(gym.ObservationWrapper):
    def fonk3(self, b1 = None):
        super(class1, self).fonk3(b1)
        b3 = self.b4.b7
        self.b4 = Box(
            b5 = self.b4.b5[0,0,0],
            b6 = self.b4.b6[0,0,0],
            b7 = [b3[2], b3[1], b3[0]]
        )
    def fonk4(self, observation):
        return observation.transpose(2, 0, 1)