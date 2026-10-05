class Brain:
    def __init__(self, capacity, cleaning_rate):
        self.memory = {}
        self.usage_count = {}
        self.capacity = capacity
        self.cleaning_rate = cleaning_rate
    def new_memory(self, name, value):
        name = str(name)
        value = int(value)
        if len(self.memory) >= self.capacity:
            self.clean_memory(name)
        self.memory[name] = value
        self.usage_count[name] = 1
    def recall_memory(self, name):
        if name in self.memory:
            self.usage_count[name] += 1
            return self.memory[name]
        else:
            return -1
    def clean_memory(self, current_iteration):
        print("Cleaning called at iteration", current_iteration)
        num_to_clean = int(self.capacity * self.cleaning_rate)
        for _ in range(num_to_clean):
            least_used_entry = min(self.usage_count.items(), key=lambda x: x[1])
            self.memory.pop(least_used_entry[0])
            self.usage_count.pop(least_used_entry[0])
brain = Brain(capacity=100, cleaning_rate=0.5)
brain.new_memory("A", 10)
brain.new_memory("B", 20)
print(brain.recall_memory("A"))
print(brain.recall_memory("C"))