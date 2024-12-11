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
class class1:
    def fonk1(self):
        pass
def fonk2(b13):
    b13.seed, b13.env_name, b13.gamma, b13.name, b13.reward_predictor, b13.reward_epsilon, \
    b13.use_s, b13.use_s_a, b13.b6 = b5[b13.a14]
    b13.b7 = b13.b7 + b13.env_name + '_' + str(b13.seed) + '_' + b13.name + 'UN' + str(
        b13.reward_epsilon)
    b13.b8 = b13.b7
    b13.b9 = 'ppo'
    b13.b10 = True
    b13.a1 = 1
    b13.a2 = 1
    b13.a3 = 2048
    b13.a4 = 1
    b13.a5 = 0.0
    b13.a6 = 3e-4
    b13.a7 = 1
    b13.a8 = 10
    b13.a9 = 100
    b13.b11 = b13.a6
    b13.a10 = 1
    b13.a11 = 1000000
    b13.a12 = 1.0
    b13.a13 = -1.0
if b12 = = "__main__":
    b13 = class1()
    b13.a14 = 0
    b13.b7 = "./logs/"
    fonk2(b13)
    print("Loaded Parameters:")
    print(vars(b13))