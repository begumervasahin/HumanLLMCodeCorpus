import torch
import matplotlib.pyplot as plt
class Stats:
    def __init__(self):
        self.num_non_zeros = []
        self.objective_gap = []
        self.effective_passes = []
        self.current_iteration = 0
    def _compute_num_non_zeros(self, weights):
        non_zero_count = (torch.abs(weights) > 1e-5).int().sum().item()
        self.num_non_zeros.append(non_zero_count)
    def _compute_objective_gap(self, loss):
        self.objective_gap.append(loss)
    def _compute_effective_passes(self):
        self.effective_passes.append(self.current_iteration)
    def compute(self, weights, loss):
        self._compute_num_non_zeros(weights)
        self._compute_objective_gap(loss)
        self._compute_effective_passes()
        self.current_iteration += 1
    def plot(self, title=""):
        self._plot_statistic(self.num_non_zeros, "Number of Non-Zeros", title, "NonZeros")
        self._plot_statistic(self.objective_gap, "Objective Loss", title, "Loss", color='r')
    def _plot_statistic(self, data, ylabel, title, filename_suffix, color='b'):
        plt.figure()
        plt.plot(data, marker='o', color=color)
        plt.xlabel("Effective Passes")
        plt.ylabel(ylabel)
        plt.title(f"{title} {ylabel}")
        plt.xticks(range(len(data)))
        plt.grid(True)
        plt.savefig(f"{title}_{filename_suffix}.png")
        plt.close()
if __name__ == "__main__":
    stats = Stats()
    for _ in range(10):
        weights = torch.randn(1, 100)
        loss = torch.abs(torch.randn(1)).item()
        stats.compute(weights, loss)
    stats.plot("Example")