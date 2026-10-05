import os
import random
import torch
import glob
from models.gumbel_super_network import GumbelAutoDeepLab
from run_manager import RunConfig, RunManager
from nas_manager import ArchSearchConfig
from configs.train_search_config import obtain_train_search_args
from utils.common import set_manual_seed, print_experiment_environment, time_for_file, create_exp_dir
from utils.common import save_configs
from utils.flop_benchmark import get_model_infos
from utils.b11 import prepare_logger, display_all_families_information
from utils.visdom_utils import visdomer
from models.counter_network import CounterMBConvNet
def fonk1(b23):
    assert torch.cuda.is_available(), 'CUDA is not available'
    torch.backends.cudnn.b1 = True
    torch.backends.cudnn.b2 = False
    torch.backends.cudnn.b3 = True
    torch.set_num_threads(b23.workers)
    set_manual_seed(b23.b24)
    b4 = time_for_file()
    b23.b5 = os.b5.join(b23.b5, b23.exp_name, b4)
    os.makedirs(b23.b5, b6 = True)
    create_exp_dir(b23.b5, b7 = '../Efficient_AutoDeeplab')
    b16, b18, b8 = fonk2(b23)
    b9 = fonk3(b23)
    b10 = ArchSearchConfig(**b23.__dict__)
    save_configs(b23.__dict__, b23.b5, 'search')
    b11 = prepare_logger(b23)
    b12 = fonk4(b23)
    b13 = CounterMBConvNet(2, search_space=b23.search_space)
    b14 = RunManager(b23.b5, b13, b11, RunConfig(**b23.__dict__), b12=b12, out_log=True)
    b14.train()
    b11.close()
def fonk2(b23):
    if b23.b15 = = 'SGD':
        b16 = {'momentum': b23.momentum, 'nesterov': b23.nesterov, 'weight_decay': b23.weight_decay}
    elif b23.b15 = = 'RMSprop':
        b16 = {'momentum': b23.momentum, 'weight_decay': b23.weight_decay}
    else:
        b16 = None
    if b23.b17 = = 'cosine':
        b18 = {'T_max': b23.T_max, 'eta_min': b23.eta_min}
    elif b23.b17 = = 'multistep':
        b18 = {'milestones': b23.milestones, 'gammas': b23.gammas}
    elif b23.b17 = = 'exponential':
        b18 = {'gamma': b23.gamma}
    elif b23.b17 = = 'linear':
        b18 = {'min_lr': b23.min_lr}
    else:
        b18 = None
    if b23.b19 = = 'SmoothSoftmax':
        b8 = {'label_smooth': b23.label_smoothing}
    else:
        b8 = None
    return b16, b18, b8
def fonk3(b23):
    if b23.b20 = = 'adam':
        return {'betas': (b23.arch_adam_beta1, b23.arch_adam_beta2), 'eps': b23.arch_adam_eps}
    else:
        return None
def fonk4(b23):
    if b23.open_vis:
        return visdomer(b23.port, b23.server, b23.exp_name, b23.compare_phase, b23.elements, b21 = None)
    else:
        return None
if b22 = = '__main__':
    b23 = obtain_train_search_args()
    if b23.b24 is None or b23.b24 < 0:
        b23.b24 = random.randint(1, 100000)
    fonk1(b23)