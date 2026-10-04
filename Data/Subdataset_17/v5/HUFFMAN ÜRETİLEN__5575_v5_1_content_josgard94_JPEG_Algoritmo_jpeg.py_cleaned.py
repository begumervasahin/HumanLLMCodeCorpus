
from scipy.fftpack import dct, idct
import numpy as np
from PIL import Image
QUANTIZATION_MATRIX = np.array([
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
frequencies = {}
index = 0
def dct2(block):
    block -= 128
    transformed = dct(dct(block, axis=0, norm='ortho'), axis=1, norm='ortho')
    quantized = np.round(transformed / QUANTIZATION_MATRIX).astype(int)
    return quantized
def zigzag(matrix):
    global index
    rows, cols = matrix.shape
    result = []
    for sum_idx in range(rows + cols - 1):
        if sum_idx % 2 == 0:
            row, col = (sum_idx, 0) if sum_idx < cols else (cols - 1, sum_idx - cols + 1)
            while row >= 0 and col < rows:
                result.append(matrix[row, col])
                row -= 1
                col += 1
        else:
            row, col = (0, sum_idx) if sum_idx < rows else (sum_idx - rows + 1, rows - 1)
            while row < cols and col >= 0:
                result.append(matrix[row, col])
                row += 1
                col -= 1
    for value in result:
        temporal[index] = value
        frequencies[value] = frequencies.get(value, 0) + 1
        index += 1
def save_probabilities(probabilities, keys, filename="result.txt"):
    with open(filename, "w") as file:
        for key in keys:
            file.write(f"{key}\t{probabilities[key]:.6f}\n")
def process_image(image_path):
    image = Image.open(image_path).convert('L')
    image.save("gray.jpg")
    width, height = image.size
    image_matrix = np.asarray(image, dtype=np.float32)
    dct_matrix = np.zeros((height, width))
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            dct_matrix[i:i+8, j:j+8] = dct2(image_matrix[i:i+8, j:j+8])
    dct_image = Image.fromarray(np.clip(dct_matrix, 0, 255).astype(np.uint8))
    dct_image.save("dct.jpg")
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            zigzag(dct_matrix[i:i+8, j:j+8])
    with open("dct.txt", "w") as file:
        for row in dct_matrix:
            file.write(" ".join(f"{abs(value) if value == -0.0 else value:.1f}" for value in row) + "\n")
    keys = list(frequencies.keys())
    elements = list(temporal.values())
    probabilities = {key: elements.count(key) / len(elements) for key in keys}
    save_probabilities(probabilities, keys)
    print("Image processing completed successfully. Probability file and DCT matrix file have been generated.")
