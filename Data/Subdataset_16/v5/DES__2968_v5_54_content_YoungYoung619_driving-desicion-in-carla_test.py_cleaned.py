
import tensorflow as tf
import numpy as np
import sys
import glob
import os
import threading
import math
import cv2
def fonk1():
    try:
        b1 = f'carla-*{sys.version_info.major}.{sys.version_info.minor}-'
        b2 = 'win-amd64' if os.name == 'nt' else 'linux-x86_64'
        b3 = glob.glob(f'**/{b1}{b2}.egg')[0]
        sys.path.append(b3)
        import carla
    except IndexError:
        raise ImportError('Please check your CARLA file.')
def fonk2():
    fonk1()
    from carla_utils.logging import logger
    from carla_utils.world_ops import *
    from carla_utils.sensor_ops import *
    from RL.DDPG.ddpg_utils import actor
    import RL.rl_utils as rl_tools
    print(2 ** 3)
if b4 = = "__main__":
    fonk2()