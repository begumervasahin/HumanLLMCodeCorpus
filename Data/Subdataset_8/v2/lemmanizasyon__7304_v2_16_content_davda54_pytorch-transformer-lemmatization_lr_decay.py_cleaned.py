class LRDecay:
    def __init__(self, optimizers, hidden_dim, base_learning_rate, warmup, initial_step=0):
        self.optimizers = optimizers
        self.dim = hidden_dim
        self.base_learning_rate = base_learning_rate
        self.warmup = warmup
        self.step = initial_step
    def __call__(self):
        self.step += 1
        if self.step < self.warmup:
            learning_rate = self.dim ** (-0.5) * self.step * self.warmup ** (-1.5) * self.base_learning_rate
        else:
            learning_rate = 0.5 * self.dim ** (-0.5) * self.step ** (-0.5) * self.base_learning_rate
        for optimizer in self.optimizers:
            for param_group in optimizer.param_groups:
                param_group["lr"] = learning_rate
        return learning_rate
optimizers = [optimizer1, optimizer2]
hidden_dim = 512
base_learning_rate = 0.001
warmup = 1000
initial_step = 0
lr_decay = LRDecay(optimizers, hidden_dim, base_learning_rate, warmup, initial_step)
current_learning_rate = lr_decay()
print("Current learning rate:", current_learning_rate)