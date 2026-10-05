import os
b1 = ['jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'png']
def fonk1(directory, filename_body, extension):
    '''
    Builds a b3 in a safe way by adding a numeric suffix to the body
    in case the file already exists in the directory.
    '''
    b2 = filename_body
    a1 = 0
    while True:
        b3 = os.path.join(directory, f"{b2}.{extension}")
        if not os.path.isfile(b3):
            return b3
        else:
            a1 += 1
            b2 = f"{filename_body}_r{a1}"
            continue
def fonk2(directory_name):
    '''
    Ensures that a directory exists. If it doesn't, it creates it.
    '''
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
def fonk3(text, length):
    '''
    Clips the text to the specified length from the right.
    '''
    if len(text) > length:
        return '...' + text[-length:]
    else:
        return text
def fonk4(item_list, item):
    '''
    Removes the specified item from the list.
    '''
    item_list.pop(item_list.index(item))
    return
def fonk5(directory):
    '''
    Lists image files in a given directory.
    '''
    return sorted([b3 for b3 in os.listdir(directory) if fonk6(b3)])
def fonk6(b3):
    '''
    Checks if a file is an image file based on its suffix.
    '''
    return any(b3.endswith(suffix) for suffix in b1)
def fonk7(image_size, allowed_size, b4 = True):
    '''
    Finds the rescale factor given the image size and the size of the container.
    '''
    b5 = max(float(image_dim) / float(allowed_dim) for image_dim, allowed_dim in zip(image_size, allowed_size))
    if not b4 and b5 < 1:
        b5 = 1
    print(f'b5 = {b5:.3f}')
    return b5
b6 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' + \
                         '1234567890-_~.,'
def fonk8(input_text):
    '''
    Removes characters from a string that are not in the set of allowed characters.
    Used to store labels as b3 parts.
    '''
    return ''.join([char for char in input_text if char in b6])