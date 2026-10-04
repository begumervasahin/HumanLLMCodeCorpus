import matplotlib.pyplot as plt
from Stats import Stats
def plot_variance(steps, dims):
    fig = plt.figure(figsize=(10, 10))
    data = Stats(steps, dims)
    if dims == 1:
        _, _, _, _, variances, _, _, step_size = data
        plt.title('Variance against step-size for a 1-dimensional walk')
        plt.scatter(step_size, variances[0])
        plt.xlabel('Step-size')
        plt.ylabel('Variances')
    elif dims == 2:
        _, _, _, _, _, _, _, _, _, _, variances, _, _, _, _, _, _, step_size = data
        plt.title('Variance against step-size for a 2-dimensional walk')
        plt.scatter(step_size, variances[2])
        plt.xlabel('Step-size')
        plt.ylabel('Variances')
    elif dims == 3:
        _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, step_size = data
        plt.title('Variance against step-size for a 3-dimensional walk')
        plt.scatter(step_size, variances[3])
        plt.xlabel('Step-size')
        plt.ylabel('Variances')
    else:
        raise ValueError("Unsupported dimension: {}. Please use dims=1, 2, or 3.".format(dims))
    plt.show()
if __name__ == '__main__':
    steps = 1000
    dims = 1
    plot_variance(steps, dims)