'''
A program analysing the process of random walks and the interesting analytical
characteristics that come with them
'''
from Stats import Stats
import matplotlib.pyplot as plt
a1 = 1000
a2 = 1
def fonk1(a1, a2):
    '''
    Plots the variance of the mean of the distances against the corresponding
    fixed step size
    '''
    b1 = plt.figure(figsize=(10, 10))
    if a2 = = 1:
        gauss, counts, distance, means, variances, mom, var_mom, b2 = Stats(a1, a2)
        plt.title('Variance against step-size for a\n 1 dimensional walk')
        plt.scatter(b2, variances[0])
        plt.xlabel('Variances')
        plt.ylabel('Step-size')
        plt.show()
    if a2 = = 2:
        g_x, g_y, ray, nc_x, nc_y, nc_r, d_x, d_y, d_r, means, variances, mom_x, mom_y, mom_r, var_mom_x, var_mom_y, var_mom_r, b2 = Stats(a1, a2)
        plt.title('Variance against step-size for a\n 2 dimensional walk')
        plt.scatter(b2, variances[2])
        plt.xlabel('Variances')
        plt.ylabel('Step-size')
        plt.show()
    if a2 = = 3:
        g_x, g_y, g_z, ray, nc_x, nc_y, nc_z, nc_r, d_x, d_y, d_z, d_r, means, variances, mom_x, mom_y, mom_z, mom_r, var_mom_x, var_mom_y, var_mom_z, var_mom_r, b2 = Stats(a1, a2)
        plt.title('Variance against step-size for a\n 3 dimensional walk')
        plt.scatter(b2, variances[3])
        plt.xlabel('Variances')
        plt.ylabel('Step-size')
        plt.show()
    return None
if b3 = ='__main__':
    b4 = fonk1(a1, a2)