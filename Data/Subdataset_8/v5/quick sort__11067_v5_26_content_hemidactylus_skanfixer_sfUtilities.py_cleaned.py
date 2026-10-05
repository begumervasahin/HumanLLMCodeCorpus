import os
PIC_SUFFIXES = ['jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'png']
def safe_build_file_name(directory, body, extension):
    '''
    Combines a directory, a filename body, and an extension
    Adds a numeric suffix to the body if the file already exists.
    '''
    new_body = body
    iter_count = 0
    while True:
        file_name = os.path.join(directory, f'{new_body}.{extension}')
        if not os.path.isfile(file_name):
            return file_name
        else:
            iter_count += 1
            new_body = f'{body}_r{iter_count:03}'
            continue
def ensure_directory_exists(directory_name):
    '''
    Creates the directory if it does not exist.
    '''
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
def right_clip_text(text, length):
    '''
    Clips the text from the right if it exceeds the specified length.
    '''
    if len(text) > length:
        return '...' + text[-length:]
    else:
        return text
def pop_item(item_list, item):
    '''
    Removes an item from the list.
    '''
    item_list.pop(item_list.index(item))
    return
def list_image_files(directory):
    '''
    Builds a sorted list of image files in the given directory.
    '''
    return sorted([file_name for file_name in os.listdir(directory) if is_picture(file_name)])
def is_picture(filename):
    '''
    Checks if the file has a supported image file extension.
    '''
    return any(filename.endswith(suffix) for suffix in PIC_SUFFIXES)
def find_rescale_factor(image_size, allowed_size, allow_zoom=True):
    '''
    Calculates the rescale factor given an image size and the size of the container.
    '''
    max_factor = max(float(image_dim) / float(allowed_dim) for image_dim, allowed_dim in zip(image_size, allowed_size))
    if not allow_zoom and max_factor < 1:
        max_factor = 1
    print(f'mFactor={max_factor:.3f}')
    return max_factor
file_name_allowed_chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' + \
                        '1234567890-_~.,'
def normalize_string(input_text):
    '''
    Strictly removes characters not in the allowed set.
    Used for storing labels as filename parts.
    '''
    return ''.join([char for char in input_text if char in file_name_allowed_chars])