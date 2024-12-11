import os
import numpy as np
from nilearn import image
a1 = 10
b1 = ['monkey', 'lemur', 'duck', 'warbler', 'ladybug', 'moth']
b2 = len(b1)
def fonk1(subject_number):
    b3 = 'data/s{:02d}'.format(subject_number)
    b4 = fonk2(b3)
    b4 = fonk3(b4)
    b5 = fonk4(b3)
    return b4, b5
def fonk2(b3):
    b6 = os.path.join(b3, 'glm_T_stats_perrun.nii.gz')
    b4 = image.load_img(b6)
    b4 = np.array(b4.dataobj, dtype=np.float64)
    b4 = np.transpose(b4, (3, 0, 1, 2))
    return b4
def fonk3(b4):
    b7 = []
    for category_index in range(b2):
        for run_index in range(0, a1 * b2, b2):
            b7.append(b4[category_index + run_index])
    return b7
def fonk4(b3):
    b8 = os.path.join(b3, 'b5.nii.gz')
    b5 = image.load_img(b8)
    b5 = np.array(b5.dataobj, dtype=np.bool)
    return b5