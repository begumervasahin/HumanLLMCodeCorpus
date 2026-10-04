import os
import torch
import json
import glob
from configs.evaluation_config import obtain_evaluation_args
from models.new_gumbel_model import NewGumbelAutoDeeplab
from utils.common import (
    set_manual_seed,
    time_for_file,
    save_configs,
    create_exp_dir,
    configs_resume
)
from run_manager import RunConfig, RunManager
from utils.logger import prepare_logger, display_all_families_information
from utils.visdom_utils import visdomer
from models.gumbel_cells import autodeeplab, proxyless, my_search_space
def main(args):
    assert torch.cuda.is_available(), 'CUDA is not available'
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = True
    torch.backends.cudnn.deterministic = True
    config_file_path = os.path.join(args.resume_file, 'retrain.config')
    assert os.path.exists(config_file_path), f'Cannot find config file: {config_file_path}'
    with open(config_file_path, 'r') as config_file:
        config_dict = json.load(config_file)
    configs_resume(args, config_dict, mode='test')
    exp_time_from_retrain = config_dict['path'].split('/')[-1].split('-resume-')[0]
    exp_time = time_for_file()
    args.path = os.path.join(args.path, args.exp_name, f'{exp_time}-evaluation-{exp_time_from_retrain}')
    torch.set_num_threads(args.workers)
    set_manual_seed(args.random_seed)
    os.makedirs(args.path, exist_ok=True)
    create_exp_dir(args.path, scripts_to_save=glob.glob('./*/*.py'))
    save_configs(args.__dict__, args.path, mode='test')
    logger = prepare_logger(args)
    logger.log(f'=> Loading configs from {config_file_path} (retrain checkpoint)')
    conv_candidates = {
        'autodeeplab': autodeeplab,
        'proxyless': proxyless,
        'my_search_space': my_search_space
    }.get(args.search_space, None)
    if conv_candidates is None:
        raise ValueError(f'Search space {args.search_space} is not supported')
    if args.reg_loss_type == 'add':
        args.reg_loss_params = {'lambda': args.reg_loss_lambda}
    elif args.reg_loss_type == 'mul':
        args.reg_loss_params = {
            'alpha': args.reg_loss_alpha,
            'beta': args.reg_loss_beta
        }
    else:
        args.reg_loss_params = None
    run_config = RunConfig(**args.__dict__)
    checkpoint_file = os.path.join(args.resume_file, 'checkpoints', f'seed-{args.random_seed}-retrain-best.pth')
    assert os.path.exists(checkpoint_file), f'Cannot find checkpoint file: {checkpoint_file}'
    logger.log(f'=> Loading checkpoint from {checkpoint_file} (retrain checkpoint)')
    checkpoint = torch.load(checkpoint_file)
    actual_path, cell_genotypes = checkpoint['actual_path'], checkpoint['cell_genotypes']
    new_genotypes = [
        (index, [(node_str, conv_candidates[select_index]) for node_str, select_index in edge_genotype])
        for index, edge_genotype in cell_genotypes
    ]
    log_str = f'Obtained actual_path and cell_genotypes:\n' \
              f'Actual_path: {actual_path}\nGenotype:\n'
    for index, genotype in new_genotypes:
        log_str += f'Index: {index}, Arch: {genotype}\n'
    logger.log(log_str, mode='info')
    args.actual_path = actual_path
    args.cell_genotypes = cell_genotypes
    normal_network = NewGumbelAutoDeeplab(
        nb_layers=args.nb_layers,
        filter_multiplier=args.filter_multiplier,
        block_multiplier=args.block_multiplier,
        steps=args.steps,
        nb_classes=args.nb_classes,
        actual_path=args.actual_path,
        cell_genotypes=args.cell_genotypes,
        search_space=args.search_space,
        affine=True
    )
    evaluation_run_manager = RunManager(args.path, normal_network, logger, run_config)
    normal_network.load_state_dict(checkpoint['state_dict'])
    display_all_families_information(args, 'retrain', evaluation_run_manager, logger)
    logger.log(f'=> Loaded checkpoint from {checkpoint_file} (retrain-best)')
    evaluation_run_manager.validate(is_test=True, use_train_mode=False)
    logger.close()
if __name__ == '__main__':
    args = obtain_evaluation_args()
    assert os.path.exists(args.resume_file), f'Cannot find resume_file: {args.resume_file}'
    main(args)