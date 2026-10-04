class LearningRateDecay:
    def __init__(self, optimizers, hidden_dim, base_lr, warmup_steps, initial_step=0):
        self.optimizers = optimizers
        self.hidden_dim = hidden_dim
        self.base_lr = base_lr
        self.warmup_steps = warmup_steps
        self.step = initial_step
    def __call__(self):
        self.step += 1
        if self.step < self.warmup_steps:
            lr = (self.hidden_dim ** -0.5) * self.step * (self.warmup_steps ** -1.5) * self.base_lr
        else:
            lr = 0.5 * (self.hidden_dim ** -0.5) * (self.step ** -0.5) * self.base_lr
        for optimizer in self.optimizers:
            for param_group in optimizer.param_groups:
                param_group["lr"] = lr
        return lr
optimizers = [optimizer1, optimizer2]
hidden_dim = 512
base_lr = 0.001
warmup_steps = 1000
lr_decay = LearningRateDecay(optimizers, hidden_dim, base_lr, warmup_steps)
current_learning_rate = lr_decay()
print("Current learning rate:", current_learning_rate)