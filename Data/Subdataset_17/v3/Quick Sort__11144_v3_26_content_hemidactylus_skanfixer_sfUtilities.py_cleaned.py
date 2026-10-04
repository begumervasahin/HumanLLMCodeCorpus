import os
PIC_SUFFIXES = ['jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'png']
def safe_build_file_name(directory, body, extension):
    new_body = body
    iteration = 0
    while True:
        file_name = os.path.join(directory, f'{new_body}.{extension}')
        if not os.path.isfile(file_name):
            return file_name
        iteration += 1
        new_body = f'{body}_r{iteration:03d}'
def ensure_directory_exists(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
def right_clip_text(text, length):
    return text if len(text) <= length else '...' + text[-length:]
def pop_item(q_list, q_item):
    q_list.pop(q_list.index(q_item))
def list_image_files(directory):
    return sorted([file_name for file_name in os.listdir(directory) if is_picture(file_name)])
def is_picture(filename):
    return any(filename.lower().endswith(suffix) for suffix in PIC_SUFFIXES)
def find_rescale_factor(img_size, allowed_size, allow_zoom=True):
    max_factor = max(float(img_dim) / float(allowed_dim) for img_dim, allowed_dim in zip(img_size, allowed_size))
    if not allow_zoom and max_factor < 1:
        max_factor = 1
    print(f'Rescale factor = {max_factor:.3f}')
    return max_factor
file_name_allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_~.,'
def normalize_string(text):
    return ''.join([char for char in text if char in file_name_allowed_chars])
if __name__ == "__main__":
    dir_path = './test_dir'
    base_name = 'image'
    file_ext = 'jpg'
    ensure_directory_exists(dir_path)
    unique_filename = safe_build_file_name(dir_path, base_name, file_ext)
    print(f'Unique filename: {unique_filename}')
    image_files = list_image_files(dir_path)
    print(f'Image files in directory: {image_files}')
    sample_text = "Hello, World! This is a test."
    normalized_text = normalize_string(sample_text)
    print(f'Normalized text: {normalized_text}')
    image_size = (1920, 1080)
    allowed_size = (800, 600)
    rescale_factor = find_rescale_factor(image_size, allowed_size)
    print(f'Rescale factor: {rescale_factor:.3f}')