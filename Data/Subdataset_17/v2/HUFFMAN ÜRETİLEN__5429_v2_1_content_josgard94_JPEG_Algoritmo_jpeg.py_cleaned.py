import numpy as np
from scipy.fftpack import dct
from PIL import Image
import os
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
temporal_values = {}
frequency_map = {}
temporal_index = 0
def apply_dct(block):
    block = block - 128
    dct_block = dct(dct(block, axis=0, norm='ortho'), axis=1, norm='ortho')
    quantized_block = np.round(dct_block / QUANTIZATION_MATRIX)
    return quantized_block
def zigzag_order(matrix):
    global temporal_index
    rows, cols = matrix.shape
    result = [[] for _ in range(rows + cols - 1)]
    for i in range(rows):
        for j in range(cols):
            sum_idx = i + j
            if sum_idx % 2 == 0:
                result[sum_idx].insert(0, matrix[i, j])
            else:
                result[sum_idx].append(matrix[i, j])
    ordered_values = [val for sublist in result for val in sublist]
    non_zero_idx = next((i for i, v in enumerate(ordered_values) if v != 0), None)
    if non_zero_idx is not None:
        for val in ordered_values[non_zero_idx:]:
            temporal_values[temporal_index] = val
            frequency_map[val] = frequency_map.get(val, 0) + 1
            temporal_index += 1
def save_probabilities_to_file(probabilities, filename="result.txt"):
    with open(filename, "w") as file:
        for key, prob in probabilities.items():
            file.write(f"{key}\t{prob}\n")
def process_image(image_path):
    global temporal_index
    img = Image.open(image_path).convert('L')
    img.save("gray.jpg")
    img.show()
    width, height = img.size
    img_array = np.asarray(img, dtype=np.float32)
    dct_result = np.zeros_like(img_array)
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            block = img_array[i:i+8, j:j+8]
            dct_result[i:i+8, j:j+8] = apply_dct(block)
    Image.fromarray(dct_result.clip(0, 255).astype(np.uint8)).save("dct.jpg")
    Image.open("dct.jpg").show()
    for i in range(0, height, 8):
        for j in range(0, width, 8):
            zigzag_order(dct_result[i:i+8, j:j+8])
    with open("dct.txt", "w") as file:
        for row in dct_result:
            file.write(" ".join(map(str, row)) + "\n")
    total_elements = list(temporal_values.values())
    probabilities = {k: total_elements.count(k) / len(total_elements) for k in frequency_map.keys()}
    save_probabilities_to_file(probabilities)
if __name__ == "__main__":
    process_image("lena.jpg")
    print("Image processing complete. Results saved to files.")