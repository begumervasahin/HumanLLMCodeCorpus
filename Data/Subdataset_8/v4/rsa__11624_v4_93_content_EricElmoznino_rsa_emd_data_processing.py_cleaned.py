import os
import numpy as np
from nilearn import image
NUM_RUNS = 10
CATEGORIES = ['monkey', 'lemur', 'duck', 'warbler', 'ladybug', 'moth']
NUM_CATEGORIES = len(CATEGORIES)
def read_subject(subject_number):
    data_directory = 'data/s{:02d}'.format(subject_number)
    brain_filename = os.path.join(data_directory, 'glm_T_stats_perrun.nii.gz')
    brain_data = image.load_img(brain_filename)
    brain_data = np.array(brain_data.dataobj, dtype=np.float64)
    brain_data = np.transpose(brain_data, (3, 0, 1, 2))
    brain_category_ordered = []
    for category_index in range(NUM_CATEGORIES):
        for run_index in range(0, NUM_RUNS * NUM_CATEGORIES, NUM_CATEGORIES):
            brain_category_ordered.append(brain_data[category_index + run_index])
    brain_data = brain_category_ordered
    vt_mask_filename = os.path.join(data_directory, 'vt_mask.nii.gz')
    vt_mask = image.load_img(vt_mask_filename)
    vt_mask = np.array(vt_mask.dataobj, dtype=np.bool)
    return brain_data, vt_mask