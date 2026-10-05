
GAMES = [
    'Hopper-v2',
    'HalfCheetah-v2',
    'Walker2d-v2',
    'Reacher-v2',
]
SEEDS = [62, 43, 97, 104, 123, 1003, 554, 221, 11, 992]
NOISE_LEVELS = [0.6, 0.7, 0.8, 0.9, 0.95]
ALGORITHMS = [
    ([0.0, .99], "PPO+", False, False, False, False),
    ([.99], "PPO", False, False, False, False),
    ([0.0, .99], "PPO+RP", True, False, False, True)
]
RUN_CONFIGURATIONS = []
for seed in SEEDS:
    for game in GAMES:
        for noise in NOISE_LEVELS:
            for (gamma, name, rp, use_s, use_s_a, use_s_a_sprime) in ALGORITHMS:
                RUN_CONFIGURATIONS.append((seed, game, gamma, name, rp, noise, use_s, use_s_a, use_s_a_sprime))
class ExperimentArgs:
    pass
def load_experiment_params(args):
    (args.seed, args.env_name, args.gamma, args.name, args.reward_predictor, args.reward_epsilon,
     args.use_s, args.use_s_a, args.use_s_a_sprime) = RUN_CONFIGURATIONS[args.run_index]
    args.log_dir = f"{args.log_dir}{args.env_name}_{args.seed}_{args.name}SN{args.reward_epsilon}"
    args.save_dir = args.log_dir
    args.algo = 'ppo'
    args.use_gae = True
    args.log_interval = 1
    args.vis_interval = 1
    args.num_steps = 2048
    args.num_processes = 1
    args.entropy = 0.0
    args.lr = 3e-4
    args.value_loss_coef = 1
    args.ppo_epoch = 10
    args.rp_burn_in = 100
    args.lr_rp = args.lr
    args.num_stack = 1
    args.num_frames = 1000000
args = ExperimentArgs()
args.run_index = 0
args.log_dir = "./logs/"
load_experiment_params(args)
print("Loaded Parameters:")
print("Seed:", args.seed)
print("Environment Name:", args.env_name)
print("Gamma:", args.gamma)
print("Name:", args.name)
print("Reward Predictor:", args.reward_predictor)
print("Reward Epsilon:", args.reward_epsilon)
print("Use S:", args.use_s)
print("Use S_A:", args.use_s_a)
print("Use S_A_SPrime:", args.use_s_a_sprime)
print("Log Directory:", args.log_dir)
print("Save Directory:", args.save_dir)
print("Algorithm:", args.algo)
