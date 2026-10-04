import numpy as np
import os
import h5py
from sklearn.decomposition import IncrementalPCA
def generate_random_batch(rows, columns):
    return np.random.rand(rows, columns)
def create_dense_dataset(batch_rows=1000, total_rows=5000, columns=1000, save_fp="dense.h5"):
    if os.path.exists(save_fp):
        os.remove(save_fp)
    with h5py.File(save_fp, mode="a") as f:
        dset = f.create_dataset('float', (total_rows, columns), dtype=np.float64)
        for i in range(total_rows
            batch_data = generate_random_batch(batch_rows, columns)
            dset[i * batch_rows:(i + 1) * batch_rows] = batch_data
    print(f"Dataset created and saved to {save_fp}")
def apply_incremental_pca(batch_rows=500, compressed_columns=200, uncompressed_fp="dense.h5", compressed_fp="compressed_dense.h5"):
    with h5py.File(uncompressed_fp, 'r') as data:
        total_rows = data["float"].shape[0]
        ipca = IncrementalPCA(n_components=compressed_columns)
        for i in range(total_rows
            batch_data = data["float"][i * batch_rows:(i + 1) * batch_rows]
            if batch_data.size == 0:
                break
            ipca.partial_fit(batch_data)
        print("Incremental PCA model fitted.")
        if os.path.exists(compressed_fp):
            os.remove(compressed_fp)
        with h5py.File(compressed_fp, mode="a") as output:
            dset = output.create_dataset('float', (total_rows, compressed_columns), dtype=np.float64)
            for i in range(total_rows
                if i * batch_rows >= total_rows:
                    break
                transformed_batch = ipca.transform(data["float"][i * batch_rows:(i + 1) * batch_rows])
                dset[i * batch_rows:(i + 1) * batch_rows] = transformed_batch
    print(f"Compressed dataset created and saved to {compressed_fp}")
if __name__ == "__main__":
    create_dense_dataset()
    apply_incremental_pca()