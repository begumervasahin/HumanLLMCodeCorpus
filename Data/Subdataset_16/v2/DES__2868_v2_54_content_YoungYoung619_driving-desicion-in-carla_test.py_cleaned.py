
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
        b1 = 'carla-*%d.%d-%s.egg' % (
            sys.version_info.major,
            sys.version_info.minor,
            'win-amd64' if os.b2 = = 'nt' else 'linux-x86_64')
        b3 = glob.glob('**/' + b1, recursive=True)[0]
        sys.path.append(b3)
        import carla
    except IndexError:
        raise ImportError('Please check your CARLA egg file path and ensure it exists.')
def fonk2():
    from carla_utils.logging import logger
    from carla_utils.world_ops import *
    from carla_utils.sensor_ops import *
def fonk3():
    from RL.DDPG.ddpg_utils import actor
    import RL.rl_utils as rl_tools
def fonk4():
    fonk1()
    fonk2()
    fonk3()
    print(2 ** 3)
if b4 = = "__main__":
    fonk4()