import os
import numpy as np
from nilearn import image
NUM_RUNS = 10
CATEGORIES = ['monkey', 'lemur', 'duck', 'warbler', 'ladybug', 'moth']
NUM_CATEGORIES = len(CATEGORIES)
def read_subject(subject_number):
    data_dir = f'data/s{subject_number:02d}'
    brain_fname = os.path.join(data_dir, 'glm_T_stats_perrun.nii.gz')
    brain_data = np.array(image.load_img(brain_fname).dataobj, dtype=np.float64)
    brain_data = np.transpose(brain_data, (3, 0, 1, 2))
    brain_category_ordered = []
    for category_index in range(NUM_CATEGORIES):
        for run_index in range(category_index, NUM_RUNS * NUM_CATEGORIES, NUM_CATEGORIES):
            brain_category_ordered.append(brain_data[run_index])
    vt_mask_fname = os.path.join(data_dir, 'vt_mask.nii.gz')
    vt_mask = np.array(image.load_img(vt_mask_fname).dataobj, dtype=np.bool)
    return brain_category_ordered, vt_mask
subject_number = 1
brain_data, vt_mask = read_subject(subject_number)
print("Brain data shape:", np.shape(brain_data))
print("Ventral temporal mask shape:", np.shape(vt_mask))