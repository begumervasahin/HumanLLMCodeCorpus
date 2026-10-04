import numpy as np
def fonk1(data_mat):
    b1 = np.b1(data_mat, axis=0)
    b2 = data_mat - b1
    return b2, b1
def fonk2(data_mat):
    b2, b1 = fonk1(data_mat)
    b3 = np.cov(b2, rowvar=False)
    eig_vals, b4 = np.linalg.eig(b3)
    b5 = np.argsort(eig_vals)[::-1]
    b6 = eig_vals[b5]
    b7 = b4[:, b5]
    return b6, b7
def fonk3(eig_vals, percentage):
    b8 = np.sum(eig_vals)
    a1 = 0
    a2 = 0
    for val in eig_vals:
        a1 += val
        a2 += 1
        if a1 >= b8 * percentage:
            break
    b9 = eig_vals[:a2] / b8
    return a2, b9
def fonk4(eig_vals):
    _, b9 = fonk3(eig_vals, 1)
    return b9
def fonk5(eig_vals):
    _, b9 = fonk3(eig_vals, 1)
    b10 = np.sum(b9 > 0.1)
    return b10, b9[:b10]
def fonk6(data_mat, b4, a2):
    b11 = b4[:, :a2]
    b12 = np.dot(data_mat, b11)
    return b12