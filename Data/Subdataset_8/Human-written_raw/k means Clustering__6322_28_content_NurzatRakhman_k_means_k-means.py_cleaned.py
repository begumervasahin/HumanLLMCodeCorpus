import math
import numpy as np
import matplotlib.pyplot as plt
DATA = np.loadtxt("data_kmeans.txt")
[OBS, FEATURES] = DATA.shape
def form_cluster(clusters):
    tresh = 1000000000
    c_obs = (OBS, clusters)
    new_data = np.zeros(c_obs)
    init = np.random.uniform(low=-10, high=10, size=(clusters, FEATURES))
    index = np.zeros(OBS)
    while True:
        for o_b in range(OBS):
            for cluster in range(clusters):
                summa = 0
                for j in range(FEATURES):
                    diff = math.pow((DATA[o_b][j] - init[cluster][j]), 2)
                    summa = summa + diff
                new_data[o_b][cluster] = summa
            index[o_b] = new_data[o_b].argmin(axis=0)
        loss = calculate_loss(new_data, index)
        if loss <= tresh:
            break
        else:
            tresh = loss
            init = re_evaluate(clusters, index)
    return new_data, index
def re_evaluate(clusters, index):
    init = np.zeros((clusters, FEATURES))
    for cluster in range(clusters):
        count = 0
        c_l = np.zeros(FEATURES)
        for f_point in range(FEATURES):
            if index[f_point] == cluster:
                for point in range(FEATURES):
                    c_l[point] += DATA[f_point][point]
                    count += 1
        for point in range(FEATURES):
            init[cluster][point] = c_l[point]/count
    return init
def calculate_loss(new_data, index):
    loss = 0
    for point in range(OBS):
        loss = loss + new_data[point][int(index[point])]
    return loss
def draw_plot(new_data, index):
    x_pos = new_data[:, 0]
    y_pos = new_data[:, 1]
    fig = plt.figure()
    a_x = fig.add_subplot(1, 1, 1)
    colors = ["
    for i in range(len(DATA)):
        a_x.scatter(x_pos[i], y_pos[i], color=colors[int(index[i])])
    plt.show()
def main():
    new_data, index = form_cluster(2)
    draw_plot(new_data, index)
if __name__ == '__main__':
    main()