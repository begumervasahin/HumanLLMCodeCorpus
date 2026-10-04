import torch
import torch.optim as optim
class LRDecay:
    def __init__(self, optimizers, hidden_dim, base_learning_rate, warmup_steps, initial_step=0):
        self.optimizers = optimizers
        self.hidden_dim = hidden_dim
        self.base_learning_rate = base_learning_rate
        self.warmup_steps = warmup_steps
        self.step = initial_step
    def update_learning_rate(self):
        self.step += 1
        learning_rate = self.calculate_learning_rate()
        self.apply_learning_rate(learning_rate)
        return learning_rate
    def calculate_learning_rate(self):
        if self.step < self.warmup_steps:
            return (self.hidden_dim ** -0.5) * (self.step * self.warmup_steps ** -1.5) * self.base_learning_rate
        else:
            return 0.5 * (self.hidden_dim ** -0.5) * (self.step ** -0.5) * self.base_learning_rate
    def apply_learning_rate(self, learning_rate):
        for optimizer in self.optimizers:
            for param_group in optimizer.param_groups:
                param_group["lr"] = learning_rate
if __name__ == "__main__":
    model_params = [torch.nn.Parameter(torch.randn(2, 2, requires_grad=True))]
    optimizer1 = optim.SGD(model_params, lr=0.01)
    optimizer2 = optim.Adam(model_params, lr=0.01)
    optimizers = [optimizer1, optimizer2]
    hidden_dim = 512
    base_learning_rate = 0.001
    warmup_steps = 1000
    initial_step = 0
    lr_decay = LRDecay(optimizers, hidden_dim, base_learning_rate, warmup_steps, initial_step)
    for _ in range(10):
        current_learning_rate = lr_decay.update_learning_rate()
        print(f"Current learning rate: {current_learning_rate}")
        for optimizer in optimizers:
            optimizer.step()