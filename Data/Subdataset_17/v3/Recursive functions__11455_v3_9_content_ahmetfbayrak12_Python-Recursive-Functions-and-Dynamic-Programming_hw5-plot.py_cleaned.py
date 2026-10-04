import matplotlib.pyplot as plt
counts = [15, 16, 18, 20, 22]
dynamic_times = [0.000281, 0.000301, 0.000350, 0.000365, 0.000381]
recursive_times = [0.527918, 1.518410, 8.469174, 54.844483, 269.672949]
def plot_data():
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    plt.plot(counts, dynamic_times, "ro-", label="Dynamic Method", color="red")
    plt.ylabel("Time (s)")
    plt.title("Performance Comparison")
    plt.legend(loc="lower right")
    plt.subplot(2, 1, 2)
    plt.plot(counts, recursive_times, "ro-", label="Recursive Method", color="red")
    plt.ylabel("Time (s)")
    plt.xlabel("Input Size (M+N)")
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    plot_data()