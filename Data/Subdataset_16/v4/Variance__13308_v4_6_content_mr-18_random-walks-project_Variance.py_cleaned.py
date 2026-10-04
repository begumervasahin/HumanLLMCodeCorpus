import matplotlib.pyplot as plt
from Stats import Stats
def fonk1(a1, b2):
    b1 = plt.figure(figsize=(10, 10))
    if b2 = = 1:
        gauss, counts, distance, means, variances, mom, var_mom, b3 = Stats(a1, b2)
        plt.title('Variance against step-size for a 1-dimensional walk')
        plt.scatter(b3, variances[0])
        plt.xlabel('Step-size')
        plt.ylabel('Variance')
    elif b2 = = 2:
        g_x, g_y, ray, nc_x, nc_y, nc_r, d_x, d_y, d_r, means, variances, mom_x, mom_y, mom_r, var_mom_x, var_mom_y, var_mom_r, b3 = Stats(a1, b2)
        plt.title('Variance against step-size for a 2-dimensional walk')
        plt.scatter(b3, variances[2])
        plt.xlabel('Step-size')
        plt.ylabel('Variance')
    elif b2 = = 3:
        g_x, g_y, g_z, ray, nc_x, nc_y, nc_z, nc_r, d_x, d_y, d_z, d_r, means, variances, mom_x, mom_y, mom_z, mom_r, var_mom_x, var_mom_y, var_mom_z, var_mom_r, b3 = Stats(a1, b2)
        plt.title('Variance against step-size for a 3-dimensional walk')
        plt.scatter(b3, variances[3])
        plt.xlabel('Step-size')
        plt.ylabel('Variance')
    plt.show()
if b4 = = '__main__':
    a1 = 1000
    b2 = 1
    fonk1(a1, b2)