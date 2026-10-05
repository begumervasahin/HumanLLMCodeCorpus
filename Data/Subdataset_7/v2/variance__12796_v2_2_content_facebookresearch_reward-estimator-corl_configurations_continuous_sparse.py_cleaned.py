
b1 = [
    'Hopper-v2',
    'HalfCheetah-v2',
    'Walker2d-v2',
    'Reacher-v2',
]
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
        for noise in b3:
            for (gamma, name, rp, use_s, use_s_a, b6) in b4:
                b5.append((seed, game, gamma, name, rp, noise, use_s, use_s_a, b6))
class class1:
    pass
def fonk1(b12):
    b12.seed, b12.env_name, b12.gamma, b12.name, b12.reward_predictor, b12.reward_epsilon, \
        b12.use_s, b12.use_s_a, b12.b6 = b5[b12.a12]
    b12.b7 = b12.b7 + b12.env_name + '_' + str(b12.seed) + '_' + b12.name + 'SN' + str(b12.reward_epsilon)
    b12.b8 = b12.b7
    b12.b9 = 'ppo'
    b12.b10 = True
    b12.a1 = 1
    b12.a2 = 1
    b12.a3 = 2048
    b12.a4 = 1
    b12.a5 = 0.0
    b12.a6 = 3e-4
    b12.a7 = 1
    b12.a8 = 10
    b12.a9 = 100
    b12.b11 = b12.a6
    b12.a10 = 1
    b12.a11 = 1000000
b12 = class1()
b12.a12 = 0
b12.b7 = "./logs/"
fonk1(b12)
print("Loaded Parameters:")
print("Seed:", b12.seed)
print("Environment Name:", b12.env_name)
print("Gamma:", b12.gamma)
print("Name:", b12.name)
print("Reward Predictor:", b12.reward_predictor)
print("Reward Epsilon:", b12.reward_epsilon)
print("Use S:", b12.use_s)
print("Use S_A:", b12.use_s_a)
print("Use S_A_SPrime:", b12.b6)
print("Log Directory:", b12.b7)
print("Save Directory:", b12.b8)
print("Algorithm:", b12.b9)
