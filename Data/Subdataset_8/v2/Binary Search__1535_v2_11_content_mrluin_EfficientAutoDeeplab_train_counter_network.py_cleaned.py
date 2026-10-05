import os
import random
import torch
from run_manager import RunConfig, RunManager
from nas_manager import ArchSearchConfig
from configs.train_search_config import obtain_train_search_args
from utils.common import set_manual_seed, time_for_file, create_exp_dir, save_configs
from models.counter_network import CounterMBConvNet
from utils.logger import prepare_logger
from utils.visdom_utils import visdomer
def main(args):
    assert torch.cuda.is_available(), 'CUDA is not available'
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    torch.set_num_threads(args.workers)
    set_manual_seed(args.random_seed)
    EXP_time = time_for_file()
    args.path = os.path.join(args.path, args.exp_name, EXP_time)
    os.makedirs(args.path, exist_ok=True)
    create_exp_dir(args.path, scripts_to_save='../Efficient_AutoDeeplab')
    weight_optimizer_params, scheduler_params, criterion_params = set_optimizer_scheduler_criteria(args)
    arch_optimizer_params = set_arch_optimizer_params(args)
    arch_search_config = ArchSearchConfig(**vars(args))
    save_configs(vars(args), args.path, 'search')
    logger = prepare_logger(args)
    vis = prepare_visdom(args)
    super_network = CounterMBConvNet(2, search_space=args.search_space)
    train_manager = RunManager(args.path, super_network, logger, RunConfig(**vars(args)), vis=vis, out_log=True)
    train_manager.train()
    logger.close()
def set_optimizer_scheduler_criteria(args):
    if args.weight_optimizer_type == 'SGD':
        weight_optimizer_params = {'momentum': args.momentum, 'nesterov': args.nesterov, 'weight_decay': args.weight_decay}
    elif args.weight_optimizer_type == 'RMSprop':
        weight_optimizer_params = {'momentum': args.momentum, 'weight_decay': args.weight_decay}
    else:
        weight_optimizer_params = None
    if args.scheduler == 'cosine':
        scheduler_params = {'T_max': args.T_max, 'eta_min': args.eta_min}
    elif args.scheduler == 'multistep':
        scheduler_params = {'milestones': args.milestones, 'gammas': args.gammas}
    elif args.scheduler == 'exponential':
        scheduler_params = {'gamma': args.gamma}
    elif args.scheduler == 'linear':
        scheduler_params = {'min_lr': args.min_lr}
    else:
        scheduler_params = None
    if args.criterion == 'SmoothSoftmax':
        criterion_params = {'label_smooth': args.label_smoothing}
    else:
        criterion_params = None
    return weight_optimizer_params, scheduler_params, criterion_params
def set_arch_optimizer_params(args):
    if args.arch_optimizer_type == 'adam':
        return {'betas': (args.arch_adam_beta1, args.arch_adam_beta2), 'eps': args.arch_adam_eps}
    else:
        return None
def prepare_visdom(args):
    if args.open_vis:
        return visdomer(args.port, args.server, args.exp_name, args.compare_phase, args.elements, init_params=None)
    else:
        return None
if __name__ == '__main__':
    args = obtain_train_search_args()
    if args.random_seed is None or args.random_seed < 0:
        args.random_seed = random.randint(1, 100000)
    main(args)