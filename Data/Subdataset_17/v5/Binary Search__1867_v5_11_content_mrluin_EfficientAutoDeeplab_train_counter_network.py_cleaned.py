
import os
import random
import torch
import glob
from models.gumbel_super_network import GumbelAutoDeepLab
from run_manager import RunConfig, RunManager
from nas_manager import ArchSearchConfig, ArchSearchRunManager
from configs.train_search_config import obtain_train_search_args
from utils.common import (
    set_manual_seed,
    print_experiment_environment,
    time_for_file,
    create_exp_dir,
    save_configs
)
from utils.flop_benchmark import get_model_infos
from utils.logger import prepare_logger, display_all_families_information
from utils.visdom_utils import visdomer
from models.counter_network import CounterMBConvNet
def main(args):
    assert torch.cuda.is_available(), 'CUDA is not available'
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    torch.set_num_threads(args.workers)
    set_manual_seed(args.random_seed)
    exp_time = time_for_file()
    args.path = os.path.join(args.path, args.exp_name, exp_time)
    os.makedirs(args.path, exist_ok=True)
    create_exp_dir(args.path, scripts_to_save='../Efficient_AutoDeeplab')
    weight_optimizer_params = configure_weight_optimizer_params(args)
    scheduler_params = configure_scheduler_params(args)
    criterion_params = configure_criterion_params(args)
    args.optimizer_config = {
        'optimizer_type': args.weight_optimizer_type,
        'optimizer_params': weight_optimizer_params,
        'scheduler': args.scheduler,
        'scheduler_params': scheduler_params,
        'criterion': args.criterion,
        'criterion_params': criterion_params,
        'init_lr': args.init_lr,
        'warmup_epoch': args.warmup_epochs,
        'epochs': args.epochs,
        'class_num': args.nb_classes,
    }
    args.conv_candidates = [
        '3x3_MBConv3', '3x3_MBConv6',
        '5x5_MBConv3', '5x5_MBConv6',
        '7x7_MBConv3', '7x7_MBConv6',
        'Zero',
    ]
    run_config = RunConfig(**args.__dict__)
    configure_architecture_optimizer_params(args)
    configure_regularization_loss_params(args)
    arch_search_config = ArchSearchConfig(**args.__dict__)
    save_configs(run_config.config, arch_search_config.config, args.path, 'search')
    logger = prepare_logger(args)
    vis = initialize_visualization(args)
    super_network = CounterMBConvNet(2, search_space=args.search_space)
    train_manager = RunManager(args.path, super_network, logger, run_config, vis=vis, out_log=True)
    train_manager.train()
    logger.close()
def configure_weight_optimizer_params(args):
    if args.weight_optimizer_type == 'SGD':
        return {
            'momentum': args.momentum,
            'nesterov': args.nesterov,
            'weight_decay': args.weight_decay,
        }
    elif args.weight_optimizer_type == 'RMSprop':
        return {
            'momentum': args.momentum,
            'weight_decay': args.weight_decay,
        }
    return None
def configure_scheduler_params(args):
    if args.scheduler == 'cosine':
        return {'T_max': args.T_max, 'eta_min': args.eta_min}
    elif args.scheduler == 'multistep':
        return {'milestones': args.milestones, 'gammas': args.gammas}
    elif args.scheduler == 'exponential':
        return {'gamma': args.gamma}
    elif args.scheduler == 'linear':
        return {'min_lr': args.min_lr}
    return None
def configure_criterion_params(args):
    if args.criterion == 'SmoothSoftmax':
        return {'label_smooth': args.label_smoothing}
    return None
def configure_architecture_optimizer_params(args):
    if args.arch_optimizer_type == 'adam':
        args.arch_optimizer_params = {
            'betas': (args.arch_adam_beta1, args.arch_adam_beta2),
            'eps': args.arch_adam_eps
        }
def configure_regularization_loss_params(args):
    if args.reg_loss_type == 'add':
        args.reg_loss_params = {'lambda': args.reg_loss_lambda}
    elif args.reg_loss_type == 'mul':
        args.reg_loss_params = {
            'alpha': args.reg_loss_alpha,
            'beta': args.reg_loss_beta
        }
def initialize_visualization(args):
    if args.open_vis:
        return visdomer(args.port, args.server, args.exp_name, args.compare_phase,
                        args.elements, init_params=None)
    return None
if __name__ == '__main__':
    args = obtain_train_search_args()
    if args.random_seed is None or args.random_seed < 0:
        args.random_seed = random.randint(1, 100000)
    main(args)