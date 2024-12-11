
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
        for noise_level in b3:
            for gamma_config in b4:
                b5.append((seed, game, *gamma_config, noise_level))
class class1:
    def fonk1(self):
        pass
def fonk2(b12):
    (b12.seed, b12.env_name, b12.gamma, b12.name, b12.reward_predictor,
     b12.reward_epsilon, b12.use_s, b12.use_s_a, b12.use_s_a_sprime,
     b12.noise_level) = b5[b12.a14]
    b12.b6 = f"{b12.b6}{b12.env_name}_{b12.seed}_{b12.name}UN{b12.reward_epsilon}"
    b12.b7 = b12.b6
    b12.b8 = 'ppo'
    b12.b9 = True
    b12.a1 = 1
    b12.a2 = 1
    b12.a3 = 2048
    b12.a4 = 1
    b12.a5 = 0.0
    b12.a6 = 3e-4
    b12.a7 = 1
    b12.a8 = 10
    b12.a9 = 100
    b12.b10 = b12.a6
    b12.a10 = 1
    b12.a11 = 1000000
    b12.a12 = 1.0
    b12.a13 = -1.0
if b11 = = "__main__":
    b12 = class1()
    b12.a14 = 0
    b12.b6 = "./logs/"
    fonk2(b12)
    print("Loaded Parameters:")
    print(vars(b12))