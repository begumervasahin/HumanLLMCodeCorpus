
import tensorflow as tf
import numpy as np
import sys
import glob
import os
import threading
import math
import cv2
def append_carla_egg_to_path():
    try:
        carla_version = f'carla-*{sys.version_info.major}.{sys.version_info.minor}-'
        platform = 'win-amd64' if os.name == 'nt' else 'linux-x86_64'
        carla_egg_path = glob.glob(f'**/{carla_version}{platform}.egg')[0]
        sys.path.append(carla_egg_path)
        import carla
    except IndexError:
        raise ImportError('Please check your CARLA file.')
def main():
    append_carla_egg_to_path()
    from carla_utils.logging import logger
    from carla_utils.world_ops import *
    from carla_utils.sensor_ops import *
    from RL.DDPG.ddpg_utils import actor
    import RL.rl_utils as rl_tools
    print(2 ** 3)
if __name__ == "__main__":
    main()