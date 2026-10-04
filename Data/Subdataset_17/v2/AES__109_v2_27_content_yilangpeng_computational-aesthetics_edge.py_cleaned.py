import os
import glob
import cv2
import random
import numpy as np
from scipy.spatial import distance
import ypoften as of
def attr_edge(img_path, tf_folder, blur_first=True, blur_size=3, threshold1=100, threshold2=250, adaptive_threshold=True, ratio1=0.4, ratio2=0.8, save_tf=True, select_random=True, n_random=1000):
    img = cv2.imread(img_path, 0)
    if blur_first:
        img = cv2.GaussianBlur(img, (blur_size, blur_size), 0)
    if adaptive_threshold:
        threshold1 = min(100, np.quantile(img, q=ratio1))
        threshold2 = max(200, np.quantile(img, q=ratio2))
        print("Edge detection thresholds:", threshold1, threshold2)
    edge = cv2.Canny(img, threshold1=threshold1, threshold2=threshold2)
    if save_tf:
        img_name = os.path.basename(img_path)
        img_save_path = os.path.join(tf_folder, "edge_canny", os.path.splitext(img_name)[0] + '.png')
        of.create_path(img_save_path)
        cv2.imwrite(img_save_path, edge)
    edge_points = np.transpose(np.nonzero(edge))
    h, w = edge.shape
    dia = np.sqrt(h**2 + w**2)
    total_edges = len(edge_points)
    edge_density = total_edges / (h * w)
    if total_edges > 0:
        if select_random:
            random.seed(42)
            edge_points = random.sample(list(edge_points), min(n_random, total_edges))
        distances = distance.pdist(edge_points, 'euclidean')
        edge_distribution = np.mean(distances) / dia
    else:
        edge_distribution = -99999
    edge_attributes = [edge_density, edge_distribution]
    print("Edge density & distribution:", edge_attributes)
    return edge_attributes
def main():
    img_folder = os.path.join('img_all', '')
    tf_folder = os.path.join('img_transform', '')
    result_path = os.path.join('img_result', 'edge.txt')
    img_paths = glob.glob(img_folder + '*')
    for idx, img_path in enumerate(img_paths):
        print("-" * 100)
        img_name = os.path.basename(img_path)
        print(idx, img_name)
        edge_data = [img_name] + attr_edge(img_path, tf_folder)
        of.save_list_to_txt(edge_data, result_path)
    print("DONE" * 50)
if __name__ == "__main__":
    main()