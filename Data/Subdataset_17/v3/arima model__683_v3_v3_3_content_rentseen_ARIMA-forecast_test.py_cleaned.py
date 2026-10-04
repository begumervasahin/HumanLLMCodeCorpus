import numpy as np
import matplotlib.pyplot as plt
def calculate_std_dev(means, lows, highs):
    return [(mean - low, high - mean) for mean, low, high in zip(means, lows, highs)]
def get_data():
    cavmp_means = [0.946601801623, 0.947113559077, 0.948454096069]
    cavmp_lows = [0.810084820106, 0.767802605805, 0.76494951005]
    cavmp_highs = [1.0, 1.0, 1.0]
    cavmp_std = calculate_std_dev(cavmp_means, cavmp_lows, cavmp_highs)
    castatic_means = [0.955477854026, 0.953211106968, 0.953266175663]
    castatic_lows = [0.616405792127, 0.515454403091, 0.435178540951]
    castatic_highs = [1.0, 1.0, 1.0]
    castatic_std = calculate_std_dev(castatic_means, castatic_lows, castatic_highs)
    static_means = [0.953938547729, 0.952260320505, 0.95265016232]
    static_lows = [0.615834126982, 0.515247980872, 0.436673392773]
    static_highs = [1.0, 1.0, 1.0]
    static_std = calculate_std_dev(static_means, static_lows, static_highs)
    return (cavmp_means, cavmp_std), (castatic_means, castatic_std), (static_means, static_std)
def plot_load_balance_comparison():
    (cavmp_means, cavmp_std), (castatic_means, castatic_std), (static_means, static_std) = get_data()
    num_methods = 3
    ind = np.arange(num_methods)
    bar_width = 0.2
    plt.bar(ind + 0.2, cavmp_means, bar_width, color='r', yerr=np.transpose(cavmp_std), capsize=5, label='CAVMP')
    plt.bar(ind + 0.4, castatic_means, bar_width, color='b', yerr=np.transpose(castatic_std), capsize=5, label='CAstatic')
    plt.bar(ind + 0.6, static_means, bar_width, color='g', yerr=np.transpose(static_std), capsize=5, label='Static')
    plt.ylabel('Utilization')
    plt.xlabel('Scale of Cloud (Racks)')
    plt.title('Load Balance Comparison')
    plt.xticks(ind + bar_width / 2 + 0.4, ['2x2', '4x4', '8x8'])
    plt.yticks(np.arange(0, 1.5, 0.2))
    plt.legend()
    plt.show()
if __name__ == "__main__":
    plot_load_balance_comparison()