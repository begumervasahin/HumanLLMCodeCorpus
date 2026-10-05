import os
import numpy as np
from nilearn import image
a1 = 10
b1 = ['monkey', 'lemur', 'duck', 'warbler', 'ladybug', 'moth']
b2 = len(b1)
def fonk1(subject_number):
    b3 = 'data/s{:02d}'.format(subject_number)
    b4 = os.path.join(b3, 'glm_T_stats_perrun.nii.gz')
    b5 = image.load_img(b4)
    b5 = np.array(b5.dataobj, dtype=np.float64)
    b5 = np.transpose(b5, (3, 0, 1, 2))
    b6 = []
    for category_index in range(b2):
        for run_index in range(0, a1 * b2, b2):
            b6.append(b5[category_index + run_index])
    b5 = b6
    b7 = os.path.join(b3, 'b8.nii.gz')
    b8 = image.load_img(b7)
    b8 = np.array(b8.dataobj, dtype=np.bool)
    return b5, b8