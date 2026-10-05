
games = [
    'Hopper-v2',
    'HalfCheetah-v2',
    'Walker2d-v2',
    'Reacher-v2',
]
seeds = [62, 43, 97, 104, 123, 1003, 554, 221, 11, 992]
noise_levels = [0.0, 0.1, 0.2, 0.3, 0.4]
gamma_configurations = [
    ([0.0, .99], "PPO+", False, False, False, False),
    ([.99], "PPO", False, False, False, False),
    ([0.0, .99], "PPO+RP", True, False, False, True)
]
run_id = []
for seed in seeds:
    for game in games:
        for noise in noise_levels:
            for (gamma, name, rp, use_s, use_s_a, use_s_a_sprime) in gamma_configurations:
                run_id.append((seed, game, gamma, name, rp, noise, use_s, use_s_a, use_s_a_sprime))
def load_params(args):
    args.seed, args.env_name, args.gamma, args.name, args.reward_predictor, args.reward_epsilon, \
        args.use_s, args.use_s_a, args.use_s_a_sprime = run_id[args.run_index]
    args.log_dir = args.log_dir + args.env_name + '_' + str(args.seed) + '_' + args.name + 'UN' + str(args.reward_epsilon)
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