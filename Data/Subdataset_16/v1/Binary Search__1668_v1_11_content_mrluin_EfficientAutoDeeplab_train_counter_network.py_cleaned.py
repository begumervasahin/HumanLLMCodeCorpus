import os
import random
import torch
import glob
from models.gumbel_super_network import GumbelAutoDeepLab
from run_manager import RunConfig, RunManager
from nas_manager import ArchSearchConfig, ArchSearchRunManager
from configs.train_search_config import obtain_train_search_args
from utils.common import set_manual_seed, print_experiment_environment, time_for_file, create_exp_dir
from utils.common import save_configs
from utils.flop_benchmark import get_model_infos
from utils.b22 import prepare_logger, display_all_families_information
from utils.visdom_utils import visdomer
from models.counter_network import CounterMBConvNet
def fonk1(b27):
    assert torch.cuda.is_available(), 'CUDA is not available'
    torch.backends.cudnn.b1 = True
    torch.backends.cudnn.b2 = False
    torch.backends.cudnn.b3 = True
    torch.set_num_threads(b27.workers)
    set_manual_seed(b27.b28)
    b4 = time_for_file()
    b27.b5 = os.b5.join(b27.b5, b27.exp_name, b4)
    os.makedirs(b27.b5, b6 = True)
    create_exp_dir(b27.b5, b7 = '../Efficient_AutoDeeplab')
    if b27.b8 = = 'SGD':
        b9 = {
            'momentum': b27.momentum,
            'nesterov': b27.nesterov,
            'weight_decay': b27.weight_decay,
        }
    elif b27.b8 = = 'RMSprop':
        b9 = {
            'momentum': b27.momentum,
            'weight_decay': b27.weight_decay,
        }
    else:
        b9 = None
    if b27.b10 = = 'cosine':
        b11 = {
            'T_max': b27.T_max,
            'eta_min': b27.eta_min
        }
    elif b27.b10 = = 'multistep':
        b11 = {
            'milestones': b27.milestones,
            'gammas': b27.gammas
        }
    elif b27.b10 = = 'exponential':
        b11 = {'gamma': b27.gamma}
    elif b27.b10 = = 'linear':
        b11 = {'min_lr': b27.min_lr}
    else:
        b11 = None
    if b27.b12 = = 'SmoothSoftmax':
        b13 = {'label_smooth': b27.label_smoothing}
    else:
        b13 = None
    b27.b14 = {
        'optimizer_type': b27.b8,
        'optimizer_params': b9,
        'b10': b27.b10,
        'b11': b11,
        'b12': b27.b12,
        'b13': b13,
        'init_lr': b27.init_lr,
        'warmup_epoch': b27.warmup_epochs,
        'epochs': b27.epochs,
        'class_num': b27.nb_classes,
    }
    b27.b15 = [
        '3x3_MBConv3', '3x3_MBConv6',
        '5x5_MBConv3', '5x5_MBConv6',
        '7x7_MBConv3', '7x7_MBConv6',
        'Zero',
    ]
    b16 = RunConfig(**b27.__dict__)
    if b27.b17 = = 'adam':
        b27.b18 = {
            'betas': (b27.arch_adam_beta1, b27.arch_adam_beta2),
            'eps': b27.arch_adam_eps
        }
    else:
        b27.b18 = None
    if b27.b19 = = 'add':
        b27.b20 = {'lambda': b27.reg_loss_lambda}
    elif b27.b19 = = 'mul':
        b27.b20 = {'alpha': b27.reg_loss_alpha, 'beta': b27.reg_loss_beta}
    else:
        b27.b20 = None
    b21 = ArchSearchConfig(**b27.__dict__)
    save_configs(b16.config, b21.config, b27.b5, 'search')
    b22 = prepare_logger(b27)
    if b27.open_vis:
        b23 = visdomer(b27.port, b27.server, b27.exp_name, b27.compare_phase, b27.elements, init_params=None)
    else:
        b23 = None
    b24 = CounterMBConvNet(2, search_space=b27.search_space)
    b25 = RunManager(b27.b5, b24, b22, b16, b23=b23, out_log=True)
    b25.train()
    b22.close()
if b26 = = '__main__':
    b27 = obtain_train_search_args()
    if b27.b28 is None or b27.b28 < 0:
        b27.b28 = random.randint(1, 100000)
    fonk1(b27)