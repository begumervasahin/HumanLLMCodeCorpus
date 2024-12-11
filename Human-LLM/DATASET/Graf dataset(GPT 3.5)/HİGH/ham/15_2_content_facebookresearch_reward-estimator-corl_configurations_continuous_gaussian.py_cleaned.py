b1 = [
     'Hopper-v2',
     'HalfCheetah-v2',
     'Walker2d-v2',
     'Reacher-v2',
    ]
b2 = [62, 43, 97, 104, 123, 1003, 554, 221, 11, 992]
b3 = [0.0, 0.1, 0.2, 0.3, 0.4]
b4 = [([0.0, .99], "PPO+", False, False, False, False),
          ([.99], "PPO", False, False, False, False),
          ([0.0, .99], "PPO+RP", True, False, False, True)
          ]
b5 = []
for seed in b2:
    for game in b1:
        for noise in b3:
                for (gamma, name, rp, use_s, use_s_a, b6) in b4:
                    b5.append((seed, game, gamma, name, rp, noise, use_s, use_s_a, b6))
def fonk1(args):
    args.seed, args.env_name, args.gamma, args.name, args.reward_predictor, args.reward_noise, \
        args.use_s, args.use_s_a, args.b6 = b5[args.run_index]
    args.b7 = args.b7 + args.env_name + '_' + str(args.seed) + '_' + args.name + 'GN' + str(args.reward_noise)
    args.b8 = args.b7
    args.b9 = 'ppo'
    args.b10 = True
    args.a1 = 1
    args.a2 = 1
    args.a3 = 2048
    args.a4 = 1
    args.a5 = 0.0
    args.a6 = 3e-4
    args.a7 = 1
    args.a8 = 10
    args.a9 = 100
    args.b11 = args.a6
    args.a10 = 1
    args.a11 = 1000000