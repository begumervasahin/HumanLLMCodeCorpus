import os
b1 = ['jpg', 'jpeg', 'bmp', 'tiff', 'gif', 'png']
def fonk1(directory, body, extension):
    b2 = body
    a1 = 0
    while True:
        b3 = os.path.join(directory, f'{b2}.{extension}')
        if not os.path.isfile(b3):
            return b3
        else:
            a1 += 1
            b2 = f'{body}_r{a1:03d}'
def fonk2(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
def fonk3(text, length):
    if len(text) > length:
        return '...' + text[-length:]
    else:
        return text
def fonk4(q_list, q_item):
    q_list.pop(q_list.index(q_item))
def fonk5(directory):
    return sorted([b3 for b3 in os.listdir(directory) if fonk6(b3)])
def fonk6(filename):
    return any(filename.lower().endswith(suffix) for suffix in b1)
def fonk7(img_size, b17, b4 = True):
    b5 = max(float(img_dim) / float(allowed_dim) for img_dim, allowed_dim in zip(img_size, b17))
    if not b4 and b5 < 1:
        b5 = 1
    print(f'Rescale b6 = {b5:.3f}')
    return b5
b7 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_~.,'
def fonk8(text):
    return ''.join([char for char in text if char in b7])
if b8 = = "__main__":
    b9 = './test_dir'
    b10 = 'image'
    b11 = 'jpg'
    fonk2(b9)
    b12 = fonk1(b9, b10, b11)
    print(f'Unique filename: {b12}')
    b13 = fonk5(b9)
    print(f'Image files in directory: {b13}')
    b14 = "Hello, World! This is a test."
    b15 = fonk8(b14)
    print(f'Normalized text: {b15}')
    b16 = (1920, 1080)
    b17 = (800, 600)
    b18 = fonk7(b16, b17)
    print(f'Rescale b6: {b18:.3f}')