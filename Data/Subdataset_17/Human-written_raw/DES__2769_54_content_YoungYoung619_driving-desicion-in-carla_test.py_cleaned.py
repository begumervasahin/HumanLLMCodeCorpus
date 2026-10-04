
import tensorflow as tf
import numpy as np
import sys, glob, os
try:
    sys.path.append(glob.glob('**/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
    import carla
except:
    raise ImportError('Please check your carla file')
from carla_utils.logging import logger
from carla_utils.world_ops import *
from carla_utils.sensor_ops import *
from RL.DDPG.ddpg_utils import actor
import RL.rl_utils as rl_tools
import threading
import math
import cv2
print(2**3)