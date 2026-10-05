import os
b1 = ['jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'png']
def fonk1(directory, body, extension):
    '''
    Combines a directory, a filename body, and an extension
    Adds a numeric suffix to the body if the file already exists.
    '''
    b2 = body
    a1 = 0
    while True:
        b3 = os.path.join(directory, f'{b2}.{extension}')
        if not os.path.isfile(b3):
            return b3
        else:
            a1 += 1
            b2 = f'{body}_r{a1:03}'
            continue
def fonk2(directory_name):
    '''
    Creates the directory if it does not exist.
    '''
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
def fonk3(text, length):
    '''
    Clips the text from the right if it exceeds the specified length.
    '''
    if len(text) > length:
        return '...' + text[-length:]
    else:
        return text
def fonk4(item_list, item):
    '''
    Removes an item from the list.
    '''
    item_list.pop(item_list.index(item))
    return
def fonk5(directory):
    '''
    Builds a sorted list of image files in the given directory.
    '''
    return sorted([b3 for b3 in os.listdir(directory) if fonk6(b3)])
def fonk6(filename):
    '''
    Checks if the file has a supported image file extension.
    '''
    return any(filename.endswith(suffix) for suffix in b1)
def fonk7(image_size, allowed_size, b4 = True):
    '''
    Calculates the rescale factor given an image size and the size of the container.
    '''
    b5 = max(float(image_dim) / float(allowed_dim) for image_dim, allowed_dim in zip(image_size, allowed_size))
    if not b4 and b5 < 1:
        b5 = 1
    print(f'b6 = {b5:.3f}')
    return b5
b7 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' + \
                        '1234567890-_~.,'
def fonk8(input_text):
    '''
    Strictly removes characters not in the allowed set.
    Used for storing labels as filename parts.
    '''
    return ''.join([char for char in input_text if char in b7])