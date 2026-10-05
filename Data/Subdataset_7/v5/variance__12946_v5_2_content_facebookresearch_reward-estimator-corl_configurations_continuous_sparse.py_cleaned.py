
b1 = ['Hopper-v2', 'HalfCheetah-v2', 'Walker2d-v2', 'Reacher-v2']
b2 = [62, 43, 97, 104, 123, 1003, 554, 221, 11, 992]
b3 = [0.6, 0.7, 0.8, 0.9, 0.95]
b4 = [
    ([0.0, .99], "PPO+", False, False, False, False),
    ([.99], "PPO", False, False, False, False),
    ([0.0, .99], "PPO+RP", True, False, False, True)
]
b5 = []
for seed in b2:
    for game in b1:
        for noise_value in b3:
            for (gamma_values, name, rp, use_s, use_s_a, use_s_a_sprime) in b4:
                b5.append((seed, game, gamma_values, name, rp, noise_value, use_s, use_s_a, use_s_a_sprime))
def fonk1(args):
    (args.seed, args.env_name, args.gamma, args.name, args.reward_predictor,
     args.reward_epsilon, args.use_s, args.use_s_a, args.use_s_a_sprime) = b5[args.run_index]
    args.b6 = f"{args.b6}{args.env_name}_{args.seed}_{args.name}SN{args.reward_epsilon}"
    args.b7 = args.b6
    args.b8 = 'ppo'
    args.b9 = True
    args.a1 = 1
    args.a2 = 1
    args.a3 = 2048
    args.a4 = 1
    args.a5 = 0.0
    args.a6 = 3e-4
    args.a7 = 1
    args.a8 = 10
    args.a9 = 100
    args.b10 = args.a6
    args.a10 = 1
    args.a11 = 1000000