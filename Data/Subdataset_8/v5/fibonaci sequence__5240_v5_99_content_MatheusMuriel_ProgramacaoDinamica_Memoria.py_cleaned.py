class Brain:
    def __init__(self, memory_limit, cleaning_rate):
        self.memory = {}
        self.usage_count = {}
        self.memory_limit = memory_limit
        self.cleaning_rate = cleaning_rate
    def add_memory(self, name, value):
        name = str(name)
        value = int(value)
        if len(self.memory) >= self.memory_limit:
            self.clean_memory()
        self.memory[name] = value
        self.usage_count[name] = 1
    def recall_memory(self, name):
        if name in self.memory:
            self.usage_count[name] += 1
            return self.memory[name]
        else:
            return -1
    def clean_memory(self):
        print("Cleaning called")
        num_to_clean = int(self.memory_limit * self.cleaning_rate)
        for _ in range(num_to_clean):
            least_used_entry = min(self.usage_count.items(), key=lambda x: x[1])
            self.memory.pop(least_used_entry[0])
            self.usage_count.pop(least_used_entry[0])
brain = Brain(memory_limit=100, cleaning_rate=0.5)
brain.add_memory("A", 10)
brain.add_memory("B", 20)
print(brain.recall_memory("A"))
print(brain.recall_memory("C"))