import numpy as np
from scipy.fftpack import dct, idct
from PIL import Image
import os
Z = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])
temporal = {}
frecuencia = {}
g = 0
def dct2(block):
    block = block - 128
    dct_block = dct(dct(block, axis=0, norm='ortho'), axis=1, norm='ortho')
    quantized_block = np.round(dct_block / Z)
    return quantized_block
def zigzag(matrix):
    global g
    rows, cols = matrix.shape
    solution = [[] for _ in range(rows + cols - 1)]
    for i in range(rows):
        for j in range(cols):
            sum_idx = i + j
            if sum_idx % 2 == 0:
                solution[sum_idx].insert(0, matrix[i][j])
            else:
                solution[sum_idx].append(matrix[i][j])
    ordered_values = [val for sublist in solution for val in sublist]
    non_zero_idx = next((i for i, v in enumerate(ordered_values) if v != 0), None)
    if non_zero_idx is not None:
        for val in ordered_values[non_zero_idx:]:
            temporal[g] = val
            if val not in frecuencia:
                frecuencia[val] = val
            g += 1
def save_probabilities(probabilities, keys):
    with open("result.txt", "w") as file:
        for key in keys:
            file.write(f"{key}\t{probabilities[key]}\n")
def process_image(image_path):
    global g
    img = Image.open(image_path).convert('L')
    img.save("gray.jpg")
    img.show()
    height, width = img.size
    img_array = np.asarray(img, dtype=np.float32)
    dct_result = np.zeros_like(img_array)
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            block = img_array[i:i+8, j:j+8]
            dct_result[i:i+8, j:j+8] = dct2(block)
    Image.fromarray(dct_result.clip(0, 255).astype(np.uint8)).save("dct.jpg")
    Image.open("dct.jpg").show()
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            zigzag(dct_result[i:i+8, j:j+8])
    with open("dct.txt", "w") as f:
        for i in range(height):
            for j in range(width):
                f.write(f"{dct_result[i, j]} ")
            f.write("\n")
    keys = list(frecuencia.keys())
    elementos = list(temporal.values())
    probabilities = {k: elementos.count(k) / len(elementos) for k in keys}
    save_probabilities(probabilities, keys)
if __name__ == "__main__":
    process_image("lena.jpg")
    print("Image processing complete. Results saved to files.")