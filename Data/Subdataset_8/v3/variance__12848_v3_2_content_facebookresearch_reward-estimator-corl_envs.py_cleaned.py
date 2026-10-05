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
def make_env(env_id, seed, rank, log_dir):
    def _thunk():
        env = gym.make(env_id)
        is_atari = hasattr(gym.envs, 'atari') and isinstance(env.unwrapped, gym.envs.atari.atari_env.AtariEnv)
        if is_atari:
            env = make_atari(env_id)
        env.seed(seed + rank)
        if log_dir is not None:
            env = bench.Monitor(env, os.path.join(log_dir, str(rank)))
        if is_atari:
            env = wrap_deepmind(env)
        obs_shape = env.observation_space.shape
        if len(obs_shape) == 3 and obs_shape[2] in [1, 3]:
            env = WrapPyTorch(env)
        return env
    return _thunk
class WrapPyTorch(gym.ObservationWrapper):
    def __init__(self, env=None):
        super(WrapPyTorch, self).__init__(env)
        obs_shape = self.observation_space.shape
        self.observation_space = Box(
            self.observation_space.low[0,0,0],
            self.observation_space.high[0,0,0],
            [obs_shape[2], obs_shape[1], obs_shape[0]]
        )
    def observation(self, observation):
        return observation.transpose(2, 0, 1)
if __name__ == "__main__":
    env_id = 'PongNoFrameskip-v4'
    seed = 123
    num_envs = 4
    log_dir = './logs'
    envs = [make_env(env_id, seed, i, log_dir) for i in range(num_envs)]
    for i, env in enumerate(envs):
        print(f"Environment {i}: {env}")
