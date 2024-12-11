'''
@author: Jingbo Lin
@contact: ljbxd180612@gmail.com
@github: github.com/mrluin
'''
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
def fonk1(b28):
    assert torch.cuda.is_available(), 'CUDA is not available'
    torch.backends.cudnn.b1 = True
    torch.backends.cudnn.b2 = False
    torch.backends.cudnn.b3 = True
    torch.set_num_threads(b28.workers)
    set_manual_seed(b28.b29)
    b4 = time_for_file()
    b28.b5 = os.b5.join(b28.b5, b28.exp_name, b4)
    os.makedirs(b28.b5, b6 = True)
    create_exp_dir(b28.b5, b7 = '../Efficient_AutoDeeplab')
    if b28.b8 = = 'SGD':
        b9 = {
            'momentum': b28.momentum,
            'nesterov': b28.nesterov,
            'weight_decay': b28.weight_decay,
        }
    elif b28.b8 = = 'RMSprop':
        b9 = {
            'momentum': b28.momentum,
            'weight_decay': b28.weight_decay,
        }
    else: b9 = None
    if b28.b10 = = 'cosine':
        b11 = {
            'T_max': b28.T_max,
            'eta_min': b28.eta_min
        }
    elif b28.b10 = = 'multistep':
        b11 = {
            'milestones': b28.milestones,
            'gammas': b28.gammas
        }
    elif b28.b10 = = 'exponential':
        b11 = {'gamma': b28.gamma}
    elif b28.b10 = = 'linear':
        b11 = {'min_lr': b28.min_lr}
    else: b11 = None
    if b28.b12 = = 'SmoothSoftmax':
        b13 = {'label_smooth': b28.label_smoothing}
    else: b13 = None
    b28.b14 = {
        'optimizer_type'   : b28.b8,
        'optimizer_params' : b9,
        'b10'        : b28.b10,
        'b11' : b11,
        'b12'        : b28.b12,
        'b13' : b13,
        'init_lr'          : b28.init_lr,
        'warmup_epoch'     : b28.warmup_epochs,
        'epochs'           : b28.epochs,
        'class_num'        : b28.nb_classes,
    }
    b28.b15 = [
        '3x3_MBConv3', '3x3_MBConv6',
        '5x5_MBConv3', '5x5_MBConv6',
        '7x7_MBConv3', '7x7_MBConv6',
        'Zero',
    ]
    b16 = RunConfig( **b28.__dict__ )
    if b28.b17 = = 'adam':
        b28.b18 = {
            'betas': (b28.arch_adam_beta1, b28.arch_adam_beta2),
            'eps': b28.arch_adam_eps
        }
    else: b28.b18 = None
    if b28.b19 = = 'add
        b28.b20 = {'lambda': b28.reg_loss_lambda}
    elif b28.b19 = = 'mul
        b28.b20 = {
            'alpha': b28.reg_loss_alpha,
            'beta': b28.reg_loss_beta
        }
    else: b28.b20 = None
    b21 = ArchSearchConfig( **b28.__dict__ )
    save_configs(b16.config, b21.config, b28.b5, 'search')
    b22 = prepare_logger(b28)
    if b28.open_vis:
        b23 = visdomer(b28.port, b28.server, b28.exp_name, b28.compare_phase,
                       b28.elements, b24 = None)
    else: b23 = None
    '''
    b25 = GumbelAutoDeepLab(
        b28.filter_multiplier, b28.block_multiplier, b28.steps,
        b28.nb_classes, b28.nb_layers, b28.bn_momentum, b28.bn_eps, b28.b15, b22
    )
    '''
    b25 = CounterMBConvNet(2, search_space=b28.search_space)
    b26 = RunManager(b28.b5, b25, b22, b16, b23=b23, out_log=True)
    b26.train()
    b22.close()
if b27 = = '__main__':
    b28 = obtain_train_search_args()
    if b28.b29 is None or b28.b29 < 0: b28.b29 = random.randint(1, 100000)
    fonk1(b28)