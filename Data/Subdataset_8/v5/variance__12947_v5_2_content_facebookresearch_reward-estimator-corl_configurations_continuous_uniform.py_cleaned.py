
GAMES = [
    'Hopper-v2',
    'HalfCheetah-v2',
    'Walker2d-v2',
    'Reacher-v2',
]
SEEDS = [62, 43, 97, 104, 123, 1003, 554, 221, 11, 992]
NOISE_LEVELS = [0.0, 0.1, 0.2, 0.3, 0.4]
GAMMA_CONFIGURATIONS = [
    ([0.0, .99], "PPO+", False, False, False, False),
    ([.99], "PPO", False, False, False, False),
    ([0.0, .99], "PPO+RP", True, False, False, True)
]
RUN_CONFIGURATIONS = []
for seed in SEEDS:
    for game in GAMES:
        for noise in NOISE_LEVELS:
            for gamma_config in GAMMA_CONFIGURATIONS:
                RUN_CONFIGURATIONS.append((seed, game, *gamma_config, noise))
def load_params(args):
    (args.seed, args.env_name, args.gamma, args.name, args.reward_predictor, args.reward_epsilon,
     args.use_s, args.use_s_a, args.use_s_a_sprime, _) = RUN_CONFIGURATIONS[args.run_index]
    args.log_dir = f"{args.log_dir}{args.env_name}_{args.seed}_{args.name}UN{args.reward_epsilon}"
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
    args.reward_high = 1.0
    args.reward_low = -1.0