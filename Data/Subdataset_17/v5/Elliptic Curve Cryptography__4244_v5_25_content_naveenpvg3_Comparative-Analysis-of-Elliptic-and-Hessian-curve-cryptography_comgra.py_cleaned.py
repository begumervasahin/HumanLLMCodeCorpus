import numpy as np
import matplotlib.pyplot as plt
def plot_performance_comparison():
    n_groups = 4
    file_sizes = [1, 8, 10, 12]
    ecc_time = [0.001567, 0.003833, 0.006130, 0.007508]
    hes_time = [0.001109, 0.001981, 0.005481, 0.005547]
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    bars_ecc = ax.bar(index, ecc_time, bar_width,
                      alpha=opacity,
                      color='white',
                      edgecolor='black',
                      label='ECC',
                      hatch='*')
    bars_hes = ax.bar(index + bar_width, hes_time, bar_width,
                      alpha=opacity,
                      color='white',
                      edgecolor='black',
                      label='Hessian',
                      hatch='
    ax.set_xlabel('File Size (bits)')
    ax.set_ylabel('Time Taken (secs)')
    ax.set_title('ECC vs Hessian Curve Performance')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(file_sizes)
    ax.legend()
    plt.show()
if __name__ == "__main__":
    plot_performance_comparison()