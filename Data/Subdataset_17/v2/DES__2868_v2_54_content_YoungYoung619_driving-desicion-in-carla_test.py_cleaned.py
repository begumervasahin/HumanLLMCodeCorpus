
import tensorflow as tf
import numpy as np
import sys
import glob
import os
import threading
import math
import cv2
def append_carla_egg_to_sys_path():
    try:
        carla_egg_pattern = 'carla-*%d.%d-%s.egg' % (
            sys.version_info.major,
            sys.version_info.minor,
            'win-amd64' if os.name == 'nt' else 'linux-x86_64')
        carla_egg_path = glob.glob('**/' + carla_egg_pattern, recursive=True)[0]
        sys.path.append(carla_egg_path)
        import carla
    except IndexError:
        raise ImportError('Please check your CARLA egg file path and ensure it exists.')
def import_carla_utils():
    from carla_utils.logging import logger
    from carla_utils.world_ops import *
    from carla_utils.sensor_ops import *
def import_rl_utils():
    from RL.DDPG.ddpg_utils import actor
    import RL.rl_utils as rl_tools
def main():
    append_carla_egg_to_sys_path()
    import_carla_utils()
    import_rl_utils()
    print(2 ** 3)
if __name__ == "__main__":
    main()