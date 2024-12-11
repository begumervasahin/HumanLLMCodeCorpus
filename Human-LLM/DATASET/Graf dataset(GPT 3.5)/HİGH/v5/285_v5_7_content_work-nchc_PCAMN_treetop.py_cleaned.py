
from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
def fonk1(file_path):
    return read_point_cloud(file_path)
def fonk2(b12):
    b1 = KNeighborsRegressor(b7=4, weights='distance', n_jobs=-1)
    b1.fit(b12.b8, b12.b9)
    return b1
def fonk3(b13, b14, b15):
    b2 = b15[:, 0] * (b14[:, 2] > 0.5)
    b3 = b13[~b2]
    b4 = b14[~b2]
    b5 = b13[b2]
    return b3, b4, b5
def fonk4(b5, b3, b4, b1):
    b6 = (b1.predict(b5) +
                       KNeighborsRegressor(b7 = 1, n_jobs=-1).fit(b3, b4).predict(b5)) / 2
    return b6
def fonk5(b11, b3, b4, b5, b6):
    b11.b8 = Vector3dVector(np.concatenate((b3, b5)))
    b11.b9 = Vector3dVector(np.concatenate((b4, b6)))
    b11.b10 = Vector3dVector()
def fonk6(b11, output_file_path):
    write_point_cloud(output_file_path, b11)
def fonk7():
    b11 = fonk1('tree.ply')
    b12 = fonk1('photo_test.ply')
    b1 = fonk2(b12)
    b13 = np.array(b11.b8)
    b14 = np.array(b11.b9)
    b15 = np.array(b11.b10)
    b3, b4, b5 = fonk3(b13, b14, b15)
    b6 = fonk4(b5, b3, b4, b1)
    fonk5(b11, b3, b4, b5, b6)
    fonk6(b11, 'corrected_tree.ply')
if b16 = = "__main__":
    fonk7()