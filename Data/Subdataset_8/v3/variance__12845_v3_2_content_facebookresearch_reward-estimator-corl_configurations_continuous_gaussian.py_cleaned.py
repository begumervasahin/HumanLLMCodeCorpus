import argparse
GAMES = ['Hopper-v2', 'HalfCheetah-v2', 'Walker2d-v2', 'Reacher-v2']
SEEDS = [62, 43, 97, 104, 123, 1003, 554, 221, 11, 992]
NOISE = [0.0, 0.1, 0.2, 0.3, 0.4]
GAMMAS = [
    ([0.0, .99], "PPO+", False, False, False, False),
    ([.99], "PPO", False, False, False, False),
    ([0.0, .99], "PPO+RP", True, False, False, True)
]
RUN_ID = [(seed, game, gamma, name, rp, noise, use_s, use_s_a, use_s_a_sprime)
          for seed in SEEDS
          for game in GAMES
          for noise in NOISE
          for (gamma, name, rp, use_s, use_s_a, use_s_a_sprime) in GAMMAS]
def load_params(args):
    (args.seed, args.env_name, args.gamma, args.name, args.reward_predictor,
     args.reward_noise, args.use_s, args.use_s_a, args.use_s_a_sprime) = RUN_ID[args.run_index]
    args.log_dir = f"{args.log_dir}{args.env_name}_{args.seed}_{args.name}GN{args.reward_noise}"
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
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to load parameters')
    parser.add_argument('--run_index', type=int, help='Index of run')
    parser.add_argument('--log_dir', type=str, help='Log directory')
    args = parser.parse_args()
    load_params(args)
    print("Loaded parameters:")
    print("Seed:", args.seed)
    print("Environment name:", args.env_name)
    print("Gamma:", args.gamma)
    print("Name:", args.name)
    print("Reward predictor:", args.reward_predictor)
    print("Reward noise:", args.reward_noise)
    print("Use s:", args.use_s)
    print("Use s_a:", args.use_s_a)
    print("Use s_a_sprime:", args.use_s_a_sprime)
    print("Log directory:", args.log_dir)
    print("Save directory:", args.save_dir)
    print("Algorithm:", args.algo)
    print("Use GAE:", args.use_gae)
    print("Log interval:", args.log_interval)
    print("Vis interval:", args.vis_interval)
    print("Number of steps:", args.num_steps)
    print("Number of processes:", args.num_processes)
    print("Entropy:", args.entropy)
    print("Learning rate:", args.lr)
    print("Value loss coefficient:", args.value_loss_coef)
    print("PPO epoch:", args.ppo_epoch)
    print("RP burn-in:", args.rp_burn_in)
    print("Learning rate for RP:", args.lr_rp)
    print("Number of stack:", args.num_stack)
    print("Number of frames:", args.num_frames)