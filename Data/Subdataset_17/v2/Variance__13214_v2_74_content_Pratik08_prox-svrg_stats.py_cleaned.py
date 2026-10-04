import torch
import matplotlib.pyplot as plt
class Stats:
    def __init__(self):
        self.num_non_zeros = []
        self.objective_gap = []
        self.effective_passes = []
        self.current_iteration = 0
    def _compute_num_non_zeros(self, w):
        non_zero_count = int((torch.abs(w) > 1e-5).int().sum().cpu().numpy())
        self.num_non_zeros.append(non_zero_count)
    def _compute_objective_gap(self, loss):
        self.objective_gap.append(loss)
    def _compute_effective_passes(self):
        self.effective_passes.append(self.current_iteration)
    def compute(self, w, loss):
        self._compute_num_non_zeros(w)
        self._compute_objective_gap(loss)
        self._compute_effective_passes()
        self.current_iteration += 1
    def plot(self, title=""):
        plt.figure()
        plt.plot(self.num_non_zeros, marker='o')
        plt.xlabel("Effective Passes")
        plt.ylabel("Number of Non-Zeros")
        plt.title(f"{title} Number of Non-Zeros")
        plt.xticks(range(len(self.num_non_zeros)))
        plt.grid(True)
        plt.savefig(f"{title}_NonZeros.png")
        plt.close()
        plt.figure()
        plt.plot(self.objective_gap, marker='o', color='r')
        plt.xlabel("Effective Passes")
        plt.ylabel("Objective Loss")
        plt.title(f"{title} Objective Loss")
        plt.xticks(range(len(self.objective_gap)))
        plt.grid(True)
        plt.savefig(f"{title}_Loss.png")
        plt.close()
if __name__ == "__main__":
    stats = Stats()
    for _ in range(10):
        weights = torch.randn(1, 100)
        loss = torch.abs(torch.randn(1)).item()
        stats.compute(weights, loss)
    stats.plot("Example")