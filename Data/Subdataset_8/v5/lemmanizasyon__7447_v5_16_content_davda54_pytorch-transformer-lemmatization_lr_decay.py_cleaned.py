class LRDecay:
    def __init__(self, optimizers, hidden_dim, base_learning_rate, warmup, initial_step=0):
        self.optimizers = optimizers
        self.hidden_dim = hidden_dim
        self.base_learning_rate = base_learning_rate
        self.warmup = warmup
        self.step = initial_step
    def __call__(self):
        self.step += 1
        if self.step < self.warmup:
            learning_rate = self._warmup_lr()
        else:
            learning_rate = self._decay_lr()
        self._update_optimizer_lr(learning_rate)
        return learning_rate
    def _warmup_lr(self):
        return self.hidden_dim ** (-0.5) * self.step * self.warmup ** (-1.5) * self.base_learning_rate
    def _decay_lr(self):
        return 0.5 * self.hidden_dim ** (-0.5) * self.step ** (-0.5) * self.base_learning_rate
    def _update_optimizer_lr(self, learning_rate):
        for optimizer in self.optimizers:
            for param_group in optimizer.param_groups:
                param_group["lr"] = learning_rate