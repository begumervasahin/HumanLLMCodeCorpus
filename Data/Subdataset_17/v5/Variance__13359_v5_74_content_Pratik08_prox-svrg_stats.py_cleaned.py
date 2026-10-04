import torch
import matplotlib.pyplot as plt
class Stats:
    def __init__(self):
        self.num_non_zeros = []
        self.objective_gap = []
        self.effective_passes = []
        self.current_iteration = 0
    def _compute_num_non_zeros(self, weights):
        num_non_zeros = int((torch.abs(weights) > 1e-5).int().sum().item())
        self.num_non_zeros.append(num_non_zeros)
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
        self._plot_num_non_zeros(title)
        self._plot_objective_gap(title)
    def _plot_num_non_zeros(self, title):
        plt.plot(self.num_non_zeros)
        plt.xlabel("Effective Passes")
        plt.ylabel("Number of Non-Zeros (NNZs)")
        plt.title(f"{title} NNZs")
        plt.xticks(range(len(self.num_non_zeros)))
        plt.savefig(f"{title}_NNZs.png")
        plt.clf()
    def _plot_objective_gap(self, title):
        plt.plot(self.objective_gap)
        plt.xlabel("Effective Passes")
        plt.ylabel("Objective Loss")
        plt.title(f"{title} Loss")
        plt.xticks(range(len(self.objective_gap)))
        plt.savefig(f"{title}_Loss.png")
        plt.clf()