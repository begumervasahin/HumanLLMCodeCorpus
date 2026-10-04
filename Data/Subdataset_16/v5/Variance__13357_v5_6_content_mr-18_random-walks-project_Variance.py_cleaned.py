import matplotlib.pyplot as plt
from Stats import Stats
def fonk1(a1, b3):
    b1 = plt.figure(figsize=(10, 10))
    b2 = Stats(a1, b3)
    if b3 = = 1:
        gauss, counts, distance, means, variances, mom, var_mom, b4 = b2
        b5 = 'Variance against step-size for a 1-dimensional walk'
        b6 = variances[0]
    elif b3 = = 2:
        g_x, g_y, ray, nc_x, nc_y, nc_r, d_x, d_y, d_r, means, variances, mom_x, mom_y, mom_r, var_mom_x, var_mom_y, var_mom_r, b4 = b2
        b5 = 'Variance against step-size for a 2-dimensional walk'
        b6 = variances[2]
    elif b3 = = 3:
        g_x, g_y, g_z, ray, nc_x, nc_y, nc_z, nc_r, d_x, d_y, d_z, d_r, means, variances, mom_x, mom_y, mom_z, mom_r, var_mom_x, var_mom_y, var_mom_z, var_mom_r, b4 = b2
        b5 = 'Variance against step-size for a 3-dimensional walk'
        b6 = variances[3]
    else:
        raise ValueError("b3 must be 1, 2, or 3")
    plt.b5(b5)
    plt.scatter(b4, b6)
    plt.xlabel('Step-size')
    plt.ylabel('Variance')
    plt.show()
if b7 = = '__main__':
    a1 = 1000
    b3 = 1
    fonk1(a1, b3)