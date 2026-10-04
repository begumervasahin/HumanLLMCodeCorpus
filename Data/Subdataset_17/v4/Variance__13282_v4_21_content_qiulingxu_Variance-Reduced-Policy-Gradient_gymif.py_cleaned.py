import gym
import sys
from VRRL import VRRL, montocarloevaluation, policy_neural_net, sgd, bs1
import copy
from log import log
class Agent:
    def __init__(self, env_name):
        self.env = gym.make(env_name)
        self.start_state = None
        self.curr_state = None
        self.step = 0
        self.flag = False
    def start_experiment(self):
        observation = self.env.reset()
        self.curr_state = observation
        self.step = 0
        self.flag = False
        return self.get_current_state()
    def get_current_state(self):
        return copy.deepcopy(self.curr_state)
    def perform_action(self, action):
        observation, reward, done, info = self.env.step(action)
        self.curr_state = observation
        self.step += 1
        if self.flag or done or self.step > self.env.spec.timestep_limit:
            self.flag = True
        else:
            self.flag = False
        return self.get_current_state(), float(reward)
    def is_experiment_end(self):
        return self.flag
def main():
    experiments = ['CartPole-v0', 'Acrobot-v1', 'MountainCar-v0', 'Pendulum-v0']
    for exp_name in experiments:
        for baseline in [True]:
            for variance_reduction in [True, False]:
                env = gym.make(exp_name)
                input_layer_size = env.observation_space.shape[0]
                hidden_layer_size = 16
                output_layer_size = env.action_space.n
                timestep_limit = env.spec.timestep_limit
                del env
                batch_size = 64
                bs1 = batch_size
                network_framework = [input_layer_size, 8, 8, output_layer_size]
                log_path = log(exp_name)
                policy_net = policy_neural_net(network_framework, batch_size)
                monte_carlo_eval = montocarloevaluation(log_path, batch_size=batch_size, baseline=baseline, vareduce=variance_reduction)
                optimizer = sgd(0.2)
                agent_instance = Agent(exp_name)
                vrrl = VRRL(policy_net, monte_carlo_eval, bs1, agent_instance, optimizer)
                vrrl.train(2000)
if __name__ == "__main__":
    main()