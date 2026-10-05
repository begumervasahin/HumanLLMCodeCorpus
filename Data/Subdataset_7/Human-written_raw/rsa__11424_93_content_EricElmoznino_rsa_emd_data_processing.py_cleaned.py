import os
import numpy as np
from nilearn import image
a1 = 10
b1 = ['monkey', 'lemur', 'duck', 'warbler', 'ladybug', 'moth']
b2 = len(b1)
def fonk1(subj_num):
    b3 = 'data/s{:02d}'.format(subj_num)
    b4 = os.path.join(b3, 'glm_T_stats_perrun.nii.gz')
    b5 = image.load_img(b4)
    b5 = np.array(b5.dataobj)
    b5 = b5.astype(np.float64)
    b5 = b5.transpose(3, 0, 1, 2)
    b6 = []
    for c in range(b2):
        for r in range(0, a1 * b2, b2):
            b6.append(b5[c + r])
    b5 = b6
    b7 = os.path.join(b3, 'b8.nii.gz')
    b8 = image.load_img(b7)
    b8 = np.array(b8.dataobj)
    b8 = b8.astype(np.bool)
    return b5, b8