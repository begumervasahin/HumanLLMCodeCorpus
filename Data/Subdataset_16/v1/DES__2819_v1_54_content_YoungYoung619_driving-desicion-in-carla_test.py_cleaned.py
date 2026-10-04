
import tensorflow as tf
import numpy as np
import sys
import glob
import os
import threading
import math
import cv2
try:
    b1 = glob.glob('**/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.b2 = = 'nt' else 'linux-x86_64'))[0]
    sys.path.append(b1)
    import carla
except IndexError:
    raise ImportError('Please check your CARLA egg file path and ensure it exists.')
from carla_utils.logging import logger
from carla_utils.world_ops import *
from carla_utils.sensor_ops import *
from RL.DDPG.ddpg_utils import actor
import RL.rl_utils as rl_tools
print(2 ** 3)