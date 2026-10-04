import numpy as np
import os
import h5py
from sklearn.decomposition import IncrementalPCA
def generate_random_batch(rows, columns):
    return np.random.rand(rows, columns)
def create_dense_dataset(batch_rows=1000, total_rows=5000, columns=1000, file_path="dense.h5"):
    if os.path.exists(file_path):
        os.remove(file_path)
    with h5py.File(file_path, mode="a") as hdf_file:
        dataset = hdf_file.create_dataset('float', (total_rows, columns), dtype=float)
        for i in range(total_rows
            batch_data = generate_random_batch(batch_rows, columns)
            dataset[i * batch_rows:(i + 1) * batch_rows] = batch_data
    print("Dense dataset created.")
def apply_incremental_pca(batch_rows=500, n_components=200, input_file="dense.h5", output_file="compressed_dense.h5"):
    with h5py.File(input_file, 'r') as input_hdf:
        total_rows = input_hdf["float"].shape[0]
        ipca = IncrementalPCA(n_components=n_components)
        for i in range(total_rows
            batch_data = input_hdf["float"][i * batch_rows:(i + 1) * batch_rows]
            if batch_data.size == 0:
                break
            ipca.partial_fit(batch_data)
        print("Incremental PCA model fitted.")
    if os.path.exists(output_file):
        os.remove(output_file)
    with h5py.File(output_file, mode="a") as output_hdf:
        transformed_dataset = output_hdf.create_dataset('float', (total_rows, n_components), dtype=float)
        with h5py.File(input_file, 'r') as input_hdf:
            for i in range(total_rows
                if i * batch_rows >= total_rows:
                    break
                batch_data = ipca.transform(input_hdf["float"][i * batch_rows:(i + 1) * batch_rows])
                transformed_dataset[i * batch_rows:(i + 1) * batch_rows] = batch_data
    print("Transformed dataset saved.")
if __name__ == "__main__":
    create_dense_dataset()
    print("Dense dataset creation completed.")
    apply_incremental_pca()
    print("Incremental PCA and transformation completed.")