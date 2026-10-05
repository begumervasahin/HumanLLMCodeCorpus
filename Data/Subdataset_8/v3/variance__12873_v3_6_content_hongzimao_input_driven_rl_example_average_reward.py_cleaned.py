from collections import deque
class AveragePerStepReward:
    def __init__(self, size):
        self.reward_record = deque(maxlen=size)
        self.time_record = deque(maxlen=size)
        self.total_reward = 0
        self.total_time = 0
    def add(self, reward, time):
        if len(self.reward_record) >= self.reward_record.maxlen:
            oldest_reward = self.reward_record.popleft()
            oldest_time = self.time_record.popleft()
            self.total_reward -= oldest_reward
            self.total_time -= oldest_time
        self.reward_record.append(reward)
        self.time_record.append(time)
        self.total_reward += reward
        self.total_time += time
    def add_list(self, list_reward, list_time):
        assert len(list_reward) == len(list_time)
        for reward, time in zip(list_reward, list_time):
            self.add(reward, time)
    def add_list_filter_zero(self, list_reward, list_time):
        assert len(list_reward) == len(list_time)
        for reward, time in zip(list_reward, list_time):
            if time != 0:
                self.add(reward, time)
            else:
                assert reward == 0
    def get_avg_per_step_reward(self):
        if self.total_time == 0:
            return 0
        else:
            return self.total_reward / self.total_time
if __name__ == "__main__":
    average_reward = AveragePerStepReward(5)
    rewards = [10, 20, 30, 40, 50]
    times = [1, 1, 1, 1, 1]
    average_reward.add_list(rewards, times)
    print("Average Reward per Step:", average_reward.get_avg_per_step_reward())