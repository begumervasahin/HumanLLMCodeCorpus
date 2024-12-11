
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
            for (gamma, name, rp, use_s, use_s_a, use_s_a_sprime) in b4:
                b5.append((seed, game, gamma, name, rp, noise, use_s, use_s_a, use_s_a_sprime))
class class1:
    pass
def fonk1(b11):
    (b11.seed, b11.env_name, b11.gamma, b11.name, b11.reward_predictor, b11.reward_epsilon,
     b11.use_s, b11.use_s_a, b11.use_s_a_sprime) = b5[b11.a12]
    b11.b6 = f"{b11.b6}{b11.env_name}_{b11.seed}_{b11.name}SN{b11.reward_epsilon}"
    b11.b7 = b11.b6
    b11.b8 = 'ppo'
    b11.b9 = True
    b11.a1 = 1
    b11.a2 = 1
    b11.a3 = 2048
    b11.a4 = 1
    b11.a5 = 0.0
    b11.a6 = 3e-4
    b11.a7 = 1
    b11.a8 = 10
    b11.a9 = 100
    b11.b10 = b11.a6
    b11.a10 = 1
    b11.a11 = 1000000
b11 = class1()
b11.a12 = 0
b11.b6 = "./logs/"
fonk1(b11)
print("Loaded Parameters:")
print("Seed:", b11.seed)
print("Environment Name:", b11.env_name)
print("Gamma:", b11.gamma)
print("Name:", b11.name)
print("Reward Predictor:", b11.reward_predictor)
print("Reward Epsilon:", b11.reward_epsilon)
print("Use S:", b11.use_s)
print("Use S_A:", b11.use_s_a)
print("Use S_A_SPrime:", b11.use_s_a_sprime)
print("Log Directory:", b11.b6)
print("Save Directory:", b11.b7)
print("Algorithm:", b11.b8)
