import argparse
b1 = [
    'Hopper-v2',
    'HalfCheetah-v2',
    'Walker2d-v2',
    'Reacher-v2',
]
b2 = [62, 43, 97, 104, 123, 1003, 554, 221, 11, 992]
b3 = [0.0, 0.1, 0.2, 0.3, 0.4]
b4 = [
    ([0.0, .99], "PPO+", False, False, False, False),
    ([.99], "PPO", False, False, False, False),
    ([0.0, .99], "PPO+RP", True, False, False, True)
]
b5 = []
for seed in b2:
    for game in b1:
        for noise in b3:
            for (gamma, name, rp, use_s, use_s_a, b6) in b4:
                b5.append((seed, game, gamma, name, rp, noise, use_s, use_s_a, b6))
def fonk1(b15):
    b15.seed, b15.env_name, b15.gamma, b15.name, b15.reward_predictor, b15.reward_noise, \
    b15.use_s, b15.use_s_a, b15.b6 = b5[b15.run_index]
    b15.b7 = b15.b7 + b15.env_name + '_' + str(b15.seed) + '_' + b15.name + 'GN' + str(
        b15.reward_noise)
    b15.b8 = b15.b7
    b15.b9 = 'ppo'
    b15.b10 = True
    b15.a1 = 1
    b15.a2 = 1
    b15.a3 = 2048
    b15.a4 = 1
    b15.a5 = 0.0
    b15.a6 = 3e-4
    b15.a7 = 1
    b15.a8 = 10
    b15.a9 = 100
    b15.b11 = b15.a6
    b15.a10 = 1
    b15.a11 = 1000000
if b12 = = "__main__":
    b13 = argparse.ArgumentParser(description='Script to load parameters')
    b13.add_argument('--run_index', b14 = int, help='Index of run')
    b13.add_argument('--b7', b14 = str, help='Log directory')
    b15 = b13.parse_args()
    fonk1(b15)
    print("Loaded parameters:")
    print("Seed:", b15.seed)
    print("Environment name:", b15.env_name)
    print("Gamma:", b15.gamma)
    print("Name:", b15.name)
    print("Reward predictor:", b15.reward_predictor)
    print("Reward noise:", b15.reward_noise)
    print("Use s:", b15.use_s)
    print("Use s_a:", b15.use_s_a)
    print("Use s_a_sprime:", b15.b6)
    print("Log directory:", b15.b7)
    print("Save directory:", b15.b8)
    print("Algorithm:", b15.b9)
    print("Use GAE:", b15.b10)
    print("Log interval:", b15.a1)
    print("Vis interval:", b15.a2)
    print("Number of steps:", b15.a3)
    print("Number of processes:", b15.a4)
    print("Entropy:", b15.a5)
    print("Learning rate:", b15.a6)
    print("Value loss coefficient:", b15.a7)
    print("PPO epoch:", b15.a8)
    print("RP burn-in:", b15.a9)
    print("Learning rate for RP:", b15.b11)
    print("Number of stack:", b15.a10)
    print("Number of frames:", b15.a11)