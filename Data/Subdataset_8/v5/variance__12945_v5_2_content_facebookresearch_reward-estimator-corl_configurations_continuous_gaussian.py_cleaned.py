
GAMES = [
    'Hopper-v2',
    'HalfCheetah-v2',
    'Walker2d-v2',
    'Reacher-v2',
]
SEEDS = [62, 43, 97, 104, 123, 1003, 554, 221, 11, 992]
NOISE_LEVELS = [0.0, 0.1, 0.2, 0.3, 0.4]
GAMMAS = [
    ([0.0, .99], "PPO+", False, False, False, False),
    ([.99], "PPO", False, False, False, False),
    ([0.0, .99], "PPO+RP", True, False, False, True)
]
run_ids = []
for seed in SEEDS:
    for game in GAMES:
        for noise in NOISE_LEVELS:
            for gamma_set in GAMMAS:
                gamma, name, rp, use_s, use_s_a, use_s_a_sprime = gamma_set
                run_ids.append((seed, game, gamma, name, rp, noise, use_s, use_s_a, use_s_a_sprime))
def load_params(args):
    seed, env_name, gamma, name, reward_predictor, reward_noise, \
    use_s, use_s_a, use_s_a_sprime = run_ids[args.run_index]
    args.log_dir = f"{args.log_dir}{env_name}_{seed}_{name}GN{reward_noise}"
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